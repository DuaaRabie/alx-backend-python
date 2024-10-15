#!/usr/bin/env python3
""" Async Comprehensions """


import asyncio
from typing import Awaitable, List
async_generator: Awaitable[List[float]] \
        = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ async comprehension function """
    result : List[float] = []
    async for i in async_generator():
        result.append(i)
    return result
