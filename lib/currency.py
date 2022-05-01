import aiohttp
import asyncio
from secret import FIXERIO_KEY

async def fetch_conversion_rate(session, from_code, to_code):
    fixer_params = {'symbols':    f"{from_code},{to_code}",
                    'access_key': FIXERIO_KEY}
    async with session.get("http://data.fixer.io/api/latest",
                           params=fixer_params) as response:
        # FIXME do better error handling
        assert response.status == 200
        data = await response.json()
        assert data.get('success')
        rates = data['rates']
        rate = rates[to_code] / rates[from_code]
        return f"{rate:.5}"

async def get_conversion_rate(from_code, to_code):
    async with aiohttp.ClientSession() as session:
        rate = await fetch_conversion_rate(session, from_code, to_code)
        return rate
