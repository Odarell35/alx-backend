#!/usr/bin/env python3
"""Module"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching system """

    def __init__(self):
        """ Initialize the LRU cache """
        super().__init__()
        self.lru_queue = []

    def put(self, key, item):
        """ Add item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_recently_used_key = self.lru_queue.pop(0)
            print("DISCARD:", least_recently_used_key)
            del self.cache_data[least_recently_used_key]

        self.cache_data[key] = item
        self.lru_queue.append(key)

    def get(self, key):
        """ Return the value linked to key """
        if key in self.cache_data:
            self.lru_queue.remove(key)
            self.lru_queue.append(key)
            return self.cache_data[key]
        else:
            return None
