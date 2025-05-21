class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def _hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set(self, key, value):
        index = self._hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        # Update if key exists
        for i, (k, v) in enumerate(self.data_map[index]):
            if k == key:
                self.data_map[index][i] = (key, value)
                return
        # ifnot append new
        self.data_map[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for k, v in self.data_map[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i, (k, v) in enumerate(self.data_map[index]):
                if k == key:
                    del self.data_map[index][i]
                    return True
        return False

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)
