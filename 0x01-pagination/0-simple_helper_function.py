#!/usr/bin/env python3
""" simple pagination helper
"""


def index_range(page: int, page_size: int) -> tuple:
    """Get start and ending position
    """
    if page == 1:
        start = page
        end = page_size
    elif page < 1 or page_size < 1:
        exit(1)
    else:
        start = ((page - 1) * page_size)
        end = (start + page_size)
    result = (start, end)

    return result
