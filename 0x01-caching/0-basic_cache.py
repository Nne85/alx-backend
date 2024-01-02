#!/usr/bin/python3
"""
This module Create a class BasicCache that inherits from
BaseCaching and is a caching system:
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class that inherits from BaseCaching and implements a
    simple caching system."""

    def put(self, key, item):
        """Adds an item to the cache if key and item are not None."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache by key."""
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
