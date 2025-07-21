class MyHashSet:
    def __init__(self):
        self.set = [False] * 1000001  # Initialize a fixed-size boolean array
    def add(self, key: int) -> None:
        self.set[key] = True
    def remove(self, key: int) -> None:
        self.set[key] = False
    def contains(self, key: int) -> bool:
        return self.set[key]

#Another approach using a list
class MyHashSet2:
    def __init__(self):
        self.set = []  # Initialize an empty list to store elements
    def add(self, key: int) -> None:
        if key not in self.set:
            self.set.append(key)
    def remove(self, key: int) -> None:
        if key in self.set:
            self.set.remove(key)
    def contains(self, key: int) -> bool:
        return key in self.set