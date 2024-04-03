#!/usr/bin/python3
""" Create LFUCache class that inherits from BaseCaching """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Define LFUCache """

    def __init__(self):
        """ Initialize LFUCache """
        self.block = []
        self.new_dict = {}
        super().__init__()

    def put(self, key, item):
        """ Assign the item to the dictionary """
        if key and item:
            if (len(self.block) >= self.MAX_ITEMS and
                    not self.cache_data.get(key)):
                remove = self.block.pop(0)
                self.new_dict.pop(remove)
                self.cache_data.pop(remove)
                print('DISCARD: {}'.format(remove))

            if self.cache_data.get(key):
                self.block.remove(key)
                self.new_dict[key] += 1
            else:
                self.new_dict[key] = 0

            initial_index = 0
            while (initial_index < len(self.block) and
                   not self.new_dict[self.block[initial_index]]):
                initial_index += 1
            self.block.insert(initial_index, key)
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value associated with the given key """
        if self.cache_data.get(key):
            self.new_dict[key] += 1
            if self.block.index(key) + 1 != len(self.block):
                while (self.block.index(key) + 1 < len(self.block) and
                       self.new_dict[key] >=
                       self.new_dict[self.block[self.block.index(key) + 1]]):
                    self.block.insert(self.block.index(key) + 1,
                                      self.block.pop(self.block.index(key)))
        return self.cache_data.get(key)
