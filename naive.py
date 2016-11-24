import json
import requests_unixsocket
base_url = "http+unix://%2Fvar%2Frun%2Fdocker.sock"

s = requests_unixsocket.Session()
r = s.get(f"{base_url}/events", stream=True)

for line in r.iter_lines():
    doc = json.loads(line)
    if doc["Action"] == "attach":
        cont = doc["id"]
        print(f"detected container {cont}")

        rr = s.get(f"{base_url}/containers/{cont}/logs?follow=1&stdout=1", stream=True)
        for line in rr.iter_lines():
            # doc = json.loads(line)
            # print(f"log entry {doc}")
            print(f"got line {line!r}")

        print(f"finished with {cont}")
