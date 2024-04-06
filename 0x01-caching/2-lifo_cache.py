#!/usr/bin/env python3
"""2-2-lifo_cache module"""

BaseCaching = __import__('base_caching.py').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class definition"""

    def __init__(self):
        super.__init__()
        self.lifo_key_list = []

    def put(self, key, item):
        """set item to cache data"""
        if key and item:
            self.cache_data[key] = item
            return
