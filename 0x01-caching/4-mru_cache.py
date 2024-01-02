#!/usr/bin/python3
"""This module create a class MRUCache that inherits from
BaseCaching and is a caching system"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """MRUCache class that implements a caching system with MRU eviction."""

    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item to the cache, evicting the MRU item if necessary."""

        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.cache_data.popitem(last=True)[0]
                print(f"DISCARD: {mru_key}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """Retrieves an item from the cache by key."""
        if key is not None:
            if key in self.cache_data:
                value = self.cache_data[key]
                self.cache_data.move_to_end(key)
                return value
            else:
                return None
        else:
            return None
