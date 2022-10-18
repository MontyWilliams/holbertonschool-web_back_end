#!/usr/bin/env python3
""" DB
"""


def list_all(mongo_collection):
    """ Get all items in a collection if any
    - if not return an empty list
    """
    return mongo_collection.find() or []


if __name__ == '__main__':
    list_all(mongo_collection)
