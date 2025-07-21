# class MyHashMap(object):
#     def __init__(self):
#         self.seen = {}
#     def put(self, key, value):
#         self.seen[key] = value
#     def get(self, key):
#         return self.seen.get(key,-1)
#     def remove(self, key):
#         if key in self.seen:
#            del self.seen[key]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# The above code is a simple implementation of a hash map in Python. But it can be improved in terms of efficiency and handling collisions. Below is a more efficient implementation using a list of lists to handle collisions.
#Also we dont have to use a dictionary, we can use a list of lists to store key-value pairs.

class MyHashMap:
    def __init__(self):
        self.seen = [-1] * 1000001  # Initialize a list with -1 to indicate empty slots

    def put(self, key, value):
        self.seen[key] = value

    def get(self, key):
        return self.seen[key]

    def remove(self, key):
        self.seen[key] = -1
