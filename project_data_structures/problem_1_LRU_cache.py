from collections import OrderedDict

class LRU_Cache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.values = OrderedDict()

    def get(self, key):
        if key not in self.values:
            return -1
        
        value = self.values.pop(key)
        self.values[key] = value
        
        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.values:
            self.values.pop(key)
            self.values[key] = value
            return

        if len(self.values) >= self.capacity:
            self.values.popitem(last=False)
            self.values[key] = value
        else:
            self.values[key] = value


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
# returns -1 because 9 is not present in the cache
print(our_cache.get(9))

our_cache.set(5, 5)
our_cache.set(6, 6)

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(3))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
our_cache.set(1, None) # None
print(our_cache.get(1))

# Test Case 2
our_cache.set(19, 999999999999999999999999)
print(our_cache.get(19)) # 999999999999999999999999

# Test Case 3
our_cache.set(-8, 1)
print(our_cache.get(-8)) # 1
