#!/usr/bin/python3
"""1-1-fifo_cache module"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class"""

    def __init__(self):
        super().__init__()
        self.key_list = []

    def put(self, key, item):
        """set a value"""
        if key and item:

            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                item_to_discard = self.key_list.pop(0)
                del self.cache_data[item_to_discard]
                print("DISCARD:", item_to_discard)

        self.cache_data[key] = item
        self.key_list.append(key)

    def get(self, key):
        """Get a value"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
