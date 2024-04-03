#!/usr/bin/env python3
"""Module"""

BaseCaching = __import__('base_caching').BaseCaching

class MRUCache(BaseCaching):
    """ MRU caching system """

    def __init__(self):
        """ Initialize the MRU cache """
        super().__init__()
        self.mru_queue = []

    def put(self, key, item):
        """ Add item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            most_recently_used_key = self.mru_queue.pop()
            print("DISCARD:", most_recently_used_key)
            del self.cache_data[most_recently_used_key]

        self.cache_data[key] = item
        self.mru_queue.append(key)

    def get(self, key):
        """ Return the value linked to key """
        if key in self.cache_data:
            self.mru_queue.remove(key)
            self.mru_queue.append(key)
            return self.cache_data[key]
        else:
            return None
