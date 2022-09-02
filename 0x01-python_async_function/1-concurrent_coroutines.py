#!/usr/bin/env python3
import asyncio
from typing import List
"""coroutines
"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawns wait_random n amount of times"""
    list = []
    list2 = []
    i = 0
    while (i < n):
        num = list.append(wait_random(max_delay))
        i += 1
    for cor in asyncio.as_completed(list):
        list2.append(await cor)
    return(list2)
