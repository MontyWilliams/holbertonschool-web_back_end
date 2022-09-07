#!/usr/bin/python3
""" Create the cache prototype
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """This class
    """
    

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
        if key and self.cache_data.get(key):
            return self.cache_data.get(key)
        return None
