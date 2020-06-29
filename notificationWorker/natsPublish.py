import asyncio
import json
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers

url = "192.168.1.105:4222"
topic = "notification"

async def run(data):
    nc = NATS()
    await nc.connect(url)
    await nc.publish(topic, json.dumps(data).encode())
    await nc.close()

def runPublisher(data):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(data))