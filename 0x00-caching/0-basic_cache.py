#!/usr/bin/python3
""" Create the cache prototype
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache inherits from base_caching.
        - extends put to add to cache
        - extends getter to get a value from cache
    """
    
    
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """ Get an item by key
        """
        try:
            return self.cache_data[key]
        except Exception:
            pass
