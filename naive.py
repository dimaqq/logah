#!/usr/bin/env python
import os
import json
import platform
import requests_unixsocket
base_url = "http+unix://%2Fvar%2Frun%2Fdocker.sock"

own_short_id = platform.node()

s = requests_unixsocket.Session()
r = s.get(f"{base_url}/events", stream=True)
r.raise_for_status()

for line in r.iter_lines():
    doc = json.loads(line)

    if doc["Action"] == "start":
        cont = doc["id"]
        try:
            name = doc["Actor"]["Attributes"]["name"]
        except ValueError:
            name = cont[:12]

        if cont.startswith(own_short_id):
            continue

        print(f"detected container {cont}")

        rr = s.get(f"{base_url}/containers/{cont}/logs?follow=1&stdout=1", stream=True)
        rr.raise_for_status()
        for line in rr.iter_lines():
            print(name, line)

        print(f"finished with {cont}")
