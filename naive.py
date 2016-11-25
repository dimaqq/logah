#!/usr/bin/env python
import os
import json
import logging
import platform
import requests_unixsocket
base_url = "http+unix://%2Fvar%2Frun%2Fdocker.sock"

logging.basicConfig(level=logging.DEBUG if os.environ.get("DEBUG") else logging.INFO)

own_short_id = platform.node()
own_id = next((line.strip().split("/")[-1] for line in open("/proc/self/cgroup") if line.startswith("1:name=")), None)
logging.debug("own container id %s short id %s", own_id, own_short_id)

s = requests_unixsocket.Session()
r = s.get(f"{base_url}/events", stream=True)
r.raise_for_status()

for line in r.iter_lines():
    doc = json.loads(line)
    logging.debug("got event %s", doc)

    if doc["Action"] == "start":
        cont = doc["id"]
        try:
            name = doc["Actor"]["Attributes"]["name"]
        except ValueError:
            name = cont[:12]

        if cont == own_id or cont.startswith(own_short_id):
            logging.debug("Skipping self %r", cont)
            continue

        print(f"detected container {cont}")

        rr = s.get(f"{base_url}/containers/{cont}/logs?follow=1&stdout=1", stream=True)
        rr.raise_for_status()
        for line in rr.iter_lines():
            logging.debug("log line %r", line)
            try:
                # Good apps/containers should log in JSON
                doc = json.loads(line)
            except ValueError:
                # Fall-back for old-school containers
                doc = dict(message=line)
            
            doc["container"] = name
            print(doc)

        print(f"finished with {cont}")
