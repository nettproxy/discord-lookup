import requests
from colorama import Fore, Style, init
import time
import threading, random
from datetime import datetime
from instances import info, success, error, warning, newlog, monokai
import aiohttp

async def n_xh(w_url, sess):
    try:
        wh_info = await get_wh_info(w_url)
        if wh_info:
            term_msg = "# YOUR WEBHOOK HAS BEEN TERMINATED BY https://discord.gg/bFE63P2qsB @here @everyone"
            async with sess.post(w_url, json={"content": term_msg}) as resp:
                if resp.status != 204:
                    pass
        else:
            pass
    except aiohttp.ClientError:
        pass
