#!/usr/bin/python3
"""This module create a class FIFOCache that inherits from BaseCaching
and is a caching system"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class that implements a caching system with FIFO eviction."""
    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adds an item to the cache, evicting the oldest item if
        necessary."""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.queue.pop(0)
                self.cache_data.pop(oldest_key)
                print(f"DISCARD: {oldest_key}")

            self.cache_data[key] = item
            self.queue.append(key

    def get(self, key):
    """Retrieves an item from the cache."""
    if key is None or key not in self_catchereturn super().get(key)
