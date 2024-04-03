#!/usr/bin/env python3
"""Module"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
  """class"""
  def __init__(self):
    """initialization"""
    super().__init__()

  def put(self, key, item):
    """method"""
    if key or item is None:
      return
      
    if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
      first_key = next(iter(self.cache_data))
      print("DISCARD:", first_key)
      del self.cache_data[first_key]
      
      self.cache_data[key] = item

def get(self, key):
        """"Must return the value in 
        self.cache_data linked to key."""
        if key:
            return self.cache_data.get(key)
