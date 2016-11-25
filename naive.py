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
logging.warn("%s", [own_short_id, own_id])

s = requests_unixsocket.Session()
r = s.get(f"{base_url}/events", stream=True)
r.raise_for_status()

for line in r.iter_lines():
    doc = json.loads(line)
    logging.debug("got event %s", doc)

    if doc["Action"] == "start":
        cont = doc["id"]
        if cont == own_id or cont.startswith(own_short_id):
            logging.debug("Skipping self %r", cont)
            continue

        print(f"detected container {cont}")

        rr = s.get(f"{base_url}/containers/{cont}/logs?follow=1&stdout=1", stream=True)
        rr.raise_for_status()
        for line in rr.iter_lines():
            logging.warn("log line %r", line)
            # doc = json.loads(line)
            # print(f"log entry {doc}")
            pass

        print(f"finished with {cont}")
