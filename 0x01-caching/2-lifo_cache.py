#!/usr/bin/env python3
"""Module"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching system """

    def __init__(self):
        """ Initialize the LIFO cache """
        super().__init__()

    def put(self, key, item):
        """ Add item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            print("DISCARD:", last_key)
            del self.cache_data[last_key]
        self.cache_data[key] = item

   def get(self, key):
     """"Must return the value in
     self.cache_data linked to key."""
     if key:
       return self.cache_data.get(key) 
