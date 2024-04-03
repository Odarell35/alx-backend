#!/usr/bin/env python3
"""Module"""

from base_caching import BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    """ LRU caching system """

    def __init__(self):
        """ Initialize the LRU cache """
        super().__init__()
        self.lru_queue = deque()

    def put(self, key, item):
        """ Add item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_recently_used_key = self.lru_queue.popleft()
            print("DISCARD:", least_recently_used_key)
            self.cache_data.pop(least_recently_used_key)

        self.cache_data[key] = item
        self.lru_queue.append(key)

    def get(self, key):
        """ Return the value linked to key """
        if key in self.cache_data:
            self.lru_queue.remove(key)
            self.lru_queue.append(key)
            return self.cache_data[key]
        return None
