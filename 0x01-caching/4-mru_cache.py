#!/usr/bin/python3
"""Create MRUCache class that inherits from BaseCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Define MRUCache """

    def __init__(self):
        """ Initialize MRUCache """
        self.lru_list = []
        super().__init__()

    def put(self, key, item):
        """ Assign the item to the dictionary """
        if key and item:
            if self.cache_data.get(key):
                self.lru_list.remove(key)
            while len(self.lru_list) >= self.MAX_ITEMS:
                remove = self.lru_list.pop()
                self.cache_data.pop(remove)
                print('DISCARD: {}'.format(remove))
            self.lru_list.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value associated with the given key """
        if self.cache_data.get(key):
            self.lru_list.remove(key)
            self.lru_list.append(key)
        return self.cache_data.get(key)
