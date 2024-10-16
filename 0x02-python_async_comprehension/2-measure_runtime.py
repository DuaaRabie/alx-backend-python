#!/usr/bin/env python3
""" Run time for four parallel comprehensions """


import asyncio
import time
from typing import List, Generator, Awaitable
async_comprehension: Awaitable[List[float]]\
         = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure runtime """
    start_time = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.perf_counter()

    return (end_time - start_time)
