#!/usr/bin/env python3
"""Async Generator"""


import asyncio
import random


async def async_generator():
    """ async generator """
    for _ in range(10):
        yield random.random() * 10
        await asyncio.sleep(1)
