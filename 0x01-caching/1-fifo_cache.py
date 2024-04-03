#!/usr/bin/python3
""" Contains FIFOCache class """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache implementation """
    def __init__(self):
        """ Instantiation """
        super().__init__()

    def put(self, key, item):
        """ assigns key & item to cache_data """
        if key or item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_item = next(iter(self.cache_data))
                print(f'DISCARD: {first_item}')
                self.cache_data.pop(first_item)
                self.cache_data[key] = item

    def get(self, key):
        """ returns the/a value in cache_data[key] """
        if not key:
            return None
        else:
            return self.cache_data.get(key)
