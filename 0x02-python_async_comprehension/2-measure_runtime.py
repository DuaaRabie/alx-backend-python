#!/usr/bin/env python3
""" Run time for four parallel comprehensions """


import asyncio
import time
from typing import List, Generator, Awaitable
async_comprehension: Generator[List[float], None, None]\
         = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure runtime """
    start_time = time.time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension())
    end_time = time.time()

    return (end_time - start_time)
