#!/usr/bin/env python3
""" 4. tasks """


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ function that returns all the delays """
    coroutines = []
    for _ in range(n):
        coroutines.append(task_wait_random(max_delay))

    delays = await asyncio.gather(*coroutines)
    return sorted(delays)
