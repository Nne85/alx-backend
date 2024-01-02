#!/usr/bin/python3
"""This module create a class LRUCache that inherits from BaseCaching and
is a caching system"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ class that represents the caching system for removing key when limit
    is reached"""

    def __init__(self):
        """initializes the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Removes the LRU item from a cache dictionary."""
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.cache_data.popitem(last=False)[0]
                print(f"DISCARD: {lru_key}")
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache by key."""
        if key is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
                return self.cache_data[key]
            else:
                return None
        else:
            return None
