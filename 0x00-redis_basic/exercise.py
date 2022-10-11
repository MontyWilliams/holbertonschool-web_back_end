#!/usr/bin/env python3
"""
Create a Cache class. This class will be used to store data in a Redis
"""


import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


class Cache:
    """ Class initialize redis as private var
         with 2 methods
    """

    def __init__(self):
        """
        Constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """  takes a data argument and returns a string. The method should
        generate a random key (e.g. using uuid), store the input data in
        Redis using the random key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
