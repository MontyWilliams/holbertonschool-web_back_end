#!/usr/bin/env python3
""" simple pagination helper
"""


def index_range(page: int, page_size: int) -> tuple:
    """Get start and ending position
    """
    start = ((page - 1) * page_size)
    end = (start + page_size)
    result = (start, end)

    return result
