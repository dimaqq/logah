import json
import platform
import asyncio
import aiohttp

own_short_id = platform.node()
# own_id = next((line.strip().split("/")[-1] for line in open("/proc/self/cgroup") if line.startswith("1:name=")), None)
own_id = None

conn = aiohttp.UnixConnector(path="/var/run/docker.sock")


async def events():
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get("http://xx/events") as resp:
            async for line in resp.content:
                doc = json.loads(line)
                if doc["Action"] == "start":
                    cont = doc["id"]
                    try:
                        name = doc["Actor"]["Attributes"]["name"]
                    except ValueError:
                        name = cont[:12]

                    if cont == own_id or cont.startswith(own_short_id):
                        continue

                    asyncio.ensure_future(logs(cont, name))


async def logs(cont, name):
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(f"http://xx/containers/{cont}/logs?follow=1&stdout=1") as resp:
            async for line in resp.content:
                print(name, line)


loop = asyncio.get_event_loop()
loop.run_until_complete(events())
