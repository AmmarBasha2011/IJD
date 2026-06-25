import time
from functools import lru_cache
from collections import OrderedDict


class LRUCache:
    def __init__(self, max_size=100, ttl=300):
        self.cache = OrderedDict()
        self.max_size = max_size
        self.ttl = ttl  # Time to live in seconds
        self.timestamps = {}
    
    def get(self, key):
        if key not in self.cache:
            return None
        
        if time.time() - self.timestamps[key] > self.ttl:
            self.delete(key)
            return None
        
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        self.timestamps[key] = time.time()
        
        if len(self.cache) > self.max_size:
            oldest_key = next(iter(self.cache))
            self.delete(oldest_key)
    
    def delete(self, key):
        if key in self.cache:
            del self.cache[key]
            del self.timestamps[key]
    
    def clear(self):
        self.cache.clear()
        self.timestamps.clear()


# Global cache instance
_global_cache = LRUCache()


def cache_get(key):
    return _global_cache.get(key)


def cache_put(key, value):
    _global_cache.put(key, value)


def cache_delete(key):
    _global_cache.delete(key)


def cache_clear():
    _global_cache.clear()


def cache_config(max_size=100, ttl=300):
    global _global_cache
    _global_cache = LRUCache(max_size, ttl)
