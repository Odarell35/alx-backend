#!/usr/bin/env python3
"""Module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching system """

    def __init__(self):
        """ Initialize the LIFO cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.order.pop()
            print("DISCARD:", last_key)
            del self.cache_data[last_key]

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Must return the value in self.cache_data linked to key """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
