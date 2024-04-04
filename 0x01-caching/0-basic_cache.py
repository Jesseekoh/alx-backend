#!/usr/bin/env python3
"""0-basic_cache module"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache class"""

    def put(self, key, item):
        """assign value to cache dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Gets value from dictionary"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
