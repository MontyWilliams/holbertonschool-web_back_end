#!/usr/bin/env python3
""" Import asy




    explain it to yourself. """
from typing import List
from time import time
from asyncio import gather
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run time for four parallel comprehensions """
    start = time()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    end = time()
    return (end - start)
