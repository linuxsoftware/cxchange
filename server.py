import sys
import time
import asyncio
from aiohttp import web
from aiohttp_rpc import rpc_server
from currency import get_conversion_rate
from outbox import send_rate_email

async def send_rate(to_email, from_code, to_code):
    """
    Look up the currency exchange rate for the given currency codes and
    email it to the given email address.
    """
    async def do_task():
        rate = await get_conversion_rate(from_code, to_code)
        await send_rate_email(to_email, from_code, to_code, rate)

    task = asyncio.create_task(do_task())
    # FIXME stop leaking task handles
    # FIXME use a queue
    return True

def create_app(argv):
    rpc_server.add_methods([send_rate])
    app = web.Application()
    app.add_routes([web.post('/rpc', rpc_server.handle_http_request),])
    return app

if __name__ == '__main__':
    app = create_app(sys.argv)
    web.run_app(app)
