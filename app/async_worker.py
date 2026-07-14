import json
import time

import asyncio


async def poll_once(client):
    time.sleep(1)
    return await client.fetch()


def parse_payload(raw):
    try:
        return json.loads(raw)
    except:
        return None
