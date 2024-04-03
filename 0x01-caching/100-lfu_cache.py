#!/usr/bin/env python3
"""Module"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU caching system """

    def __init__(self):
        """ Initialize the LFU cache """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Add item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lowfrequency = min(self.frequency.values())
            min_frequency = [k for k, v in self.frequency.items() if v == lowfrequency]
            least_recently = min(min_frequency, key=lambda k: self.cache_data[k])
            print("DISCARD:", least_recently)
            del self.cache_data[least_recently]
            del self.frequency[least_recently]

        self.cache_data[key] = item
        self.frequency[key] = 0

    def get(self, key):
        """ Return the value linked to key """
        if key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        else:
            return None
