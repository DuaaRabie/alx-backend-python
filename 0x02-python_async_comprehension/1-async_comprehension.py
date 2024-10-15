#!/usr/bin/env python3
""" Async Comprehensions """


import asyncio
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[None, None, List[float]]:
    """ async comprehension function """
    result = []
    async for i in async_generator():
        result.append(i)
    return result
