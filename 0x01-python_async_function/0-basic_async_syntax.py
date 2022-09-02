#!/usr/bin/env python3
""" asyncio
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """async call to wait"""
    return(random.uniform(0, max_delay))

asyncio.run(wait_random())
