#!/usr/bin/env python3
"""coroutines """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Let's execute multiple coroutines at the same time with async  """
    listDelay = [task_wait_random(max_delay) for i in range(n)]
    inOrder = []
    for delay in asyncio.as_completed(listDelay):
        inOrder.append(await delay)
    return inOrder
