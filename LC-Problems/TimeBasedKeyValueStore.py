class TimeMap:
    def __init__(self):
        self.store = {}  # key -> list of [value, timestamp]  # Initialize the store dictionary/Hashmap

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store: # Add the key if it doesn't exist
            self.store[key] = []
        self.store[key].append([value, timestamp])  # Append the value and timestamp

    def get(self, key: str, timestamp: int) -> str:
        res = "" # Retrieve the list of values for the given key
        values = self.store.get(key, [])
        l, r = 0, len(values) - 1 # Binary search to find the closest timestamp ≤ given timestamp  # noqa: E741
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp: # If the timestamp at mid is ≤ target timestamp
                res = values[m][0]  # Update result to the current value
                l = m + 1  # Move to the right to find a more recent value  # noqa: E741
            else:
                r = m - 1  # Move left to find an earlier timestamp
        return res # Return the most recent value found or an empty string if none exists

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)