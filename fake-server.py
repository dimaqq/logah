#!/usr/bin/env python
import os
import time
import json
import socket
import logging
import threading


logging.basicConfig(level=logging.DEBUG if os.environ.get("DEBUG") else logging.INFO)


class Connection(threading.Thread):
    def __init__(self, sock):
        super().__init__()
        self.sock = sock

    def run(self):
        # read and log HTTP request
        with self.sock:
            r = self.sock.makefile(mode="r", encoding="utf-8")
            w = self.sock.makefile(mode="w", encoding="utf-8")
            for line in r:
                logging.debug("read %r", line)
                if not line.strip():
                    break

            print("HTTP/1.1 200 OK", end="\r\n", file=w)
            print("Foo: bar", end="\r\n", file=w)
            print("", end="\r\n", file=w)
            w.flush()

            for i in range(1000):
                time.sleep(0.3)
                print(json.dumps(dict(fd=self.sock.fileno(), time=time.time())), file=w)
                w.flush()
                logging.debug("sent data on channel %s", self.sock.fileno())


os.unlink("./test.sock")

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.bind("./test.sock")
sock.listen(1)
while True:
    conn, addr = sock.accept()
    c = Connection(conn)
    c.start()
