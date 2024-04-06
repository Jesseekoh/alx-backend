#!/usr/bin/env python3
"""2-2-lifo_cache module"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class definition"""

    def __init__(self):
        super().__init__()
        self.lifo_key_list = []

    def put(self, key, item):
        """set item to cache data"""
        if key and item:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                item_to_discard = self.lifo_key_list.pop(-1)
                del self.cache_data[item_to_discard]
                print("DISCARD:", item_to_discard)

            self.cache_data[key] = item
            self.lifo_key_list.append(key)

    def get(self, key):
        """get item from cache"""
        if key in self.cache_data:
            return self.cache_data[key]
