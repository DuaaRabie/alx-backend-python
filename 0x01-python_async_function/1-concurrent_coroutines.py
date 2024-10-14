#!/usr/bin/env python3
""" execute multiple coroutines at the same time with async """


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ function that returns all the delays """
    coroutines = []
    for _ in range(n):
        coroutines.append(wait_random(max_delay))

    delays = await asyncio.gather(*coroutines)
    return sorted(delays)
