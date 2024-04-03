#!/usr/bin/env python3
""" Contains basic cache class """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCach class implementation """

    def __init__(self):
        """ Instantiation """
        self.cache_data = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if not key:
            return None
        return self.cache_data.get(key)
