#!/usr/bin/env python
import json
import platform
import requests_unixsocket
base_url = "http+unix://%2Fvar%2Frun%2Fdocker.sock"

own_short_id = platform.node()

s = requests_unixsocket.Session()
r = s.get(f"{base_url}/events", stream=True)

for line in r.iter_lines():
    doc = json.loads(line)

    if doc["Action"] == "start":
        cont = doc["id"][:12]

        if cont == own_short_id:
            continue

        print(f"{cont} appeared")

        rr = s.get(f"{base_url}/containers/{cont}/logs?follow=1&stdout=1", stream=True)
        for line in rr.iter_lines():
            print(f"{cont} says: {line}")

        print(f"{cont} disappeared")
