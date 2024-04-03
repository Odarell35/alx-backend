#!/usr/bin/env python3
"""Module implementation of cache system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class that inherits from BaseCaching
    and is a caching system:"""
     def __init__(self):
        """ Instantiation """
        self.cache_data = {}

    def put(self, key, item):
        """Must assign to the dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """"Must return the value in
        self.cache_data linked to key."""
        if key:
            return self.cache_data.get(key)
        else:
            return None
