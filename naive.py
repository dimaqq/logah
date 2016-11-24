import json
import logging
import requests_unixsocket
base_url = "http+unix://%2Fvar%2Frun%2Fdocker.sock"

s = requests_unixsocket.Session()
r = s.get(f"{base_url}/events", stream=True)
r.raise_for_status()

for line in r.iter_lines():
    doc = json.loads(line)
    logging.debug("got event %s", doc)

    if doc["Action"] == "start":
        cont = doc["id"]
        print(f"detected container {cont}")

        rr = s.get(f"{base_url}/containers/{cont}/logs?follow=1&stdout=1", stream=True)
        rr.raise_for_status()
        for line in rr.iter_lines():
            logging.warn("log line %r", line)
            # doc = json.loads(line)
            # print(f"log entry {doc}")
            pass

        print(f"finished with {cont}")
