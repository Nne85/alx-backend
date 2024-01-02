#!/usr/bin/python3
""" This module create a class LIFOCache that inherits from BaseCaching
and is a caching system"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class that implements a caching system with LIFO eviction."""

    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Adds an item to the cache, evicting the most recent item
        if necessary."""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.keys.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """Retrieves an item from the cache by key."""
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
