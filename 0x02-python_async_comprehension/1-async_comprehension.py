#!/usr/bin/env python3
""" Async Comprehensions """


import asyncio
from typing import Generator, List
async_generator: Generator[float, None, None] \
        = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ async comprehension function """
    return [gen async for gen in async_generator()]
