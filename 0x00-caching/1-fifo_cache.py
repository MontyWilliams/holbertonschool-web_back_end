#!/usr/bin/python3
""" Create a class LIFOCache that inherits from BaseCaching and is a caching sys.
"""
from collections import deque
BaseCaching = __import__('0-basic_cache').BaseCaching


class FIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching
        - put is extended utilizing LIFOCache algorithm
        - get is extended to get value from cache by key
    """
    
    def __init__(self):
        """ Initiliaze"""
        super().__init__()
        self.queue = deque([])

    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data the item value for the key key.
            - If key or item is None, this method should not do anything.
            - If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
                you must discard the first item put in cache (FIFO algorithm)
                you must print DISCARD: with the key discarded and following by a new line
        """
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS and key not in\
                    self.queue:
                del_key = self.queue.popleft()
                del self.cache_data[del_key]
                print("DISCARD: {}".format(del_key))
            self.cache_data[key] = item
            self.queue.append(key)
        
            

    def get(self, key):
        """ Must return the value in self.cache_data linked to key.
            - If key is None or if the key doesn’t exist in self.cache_data, return None.
        """
        try:
            return self.cache_data[key]
        except Exception:
            pass


