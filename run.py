#!/bin/env python
import sys
import os
from aiohttp import web
from pathlib import Path

here = Path(__file__).resolve().parent
os.chdir(here)
sys.path.append(f"{here}/lib")

from server import create_app

if __name__ == '__main__':
    app = create_app(sys.argv)
    web.run_app(app)
