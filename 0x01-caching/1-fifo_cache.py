#!/usr/bin/env python3
"""Contains FIFOCache class"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache implementation"""
    def __init__(self):
        """Initialization"""
        super().__init__()

    def put(self, key, item):
        """Assigns key & item to cache_data"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f'DISCARD: {first_key}')
                self.cache_data.pop(first_key)
                self.cache_data[key] = item
   
    def get(self, key):
        """Returns the/a value in cache_data[key]"""
        if not key:
            return None
        else:
            return self.cache_data.get(key)
