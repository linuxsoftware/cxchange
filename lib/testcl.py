import sys
import asyncio
from aiohttp_rpc import JsonRpcClient
from secret import TEST_EMAIL_ADDRESS

async def run():
    async with JsonRpcClient('http://localhost:8080/rpc') as rpc:
        await rpc.send_rate(TEST_EMAIL_ADDRESS, "NZD", "GBP")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
