class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def set(self, key, value):
        hash_index = self._hash(key)
        if self.table[hash_index] is None:
            self.table[hash_index] = [(key, value)]
        else:
            for pair in self.table[hash_index]:
                if pair[0] == key:
                    pair = (key, value)
                    break
            else:
                self.table[hash_index].append((key, value))

    def get(self, key):
        hash_index = self._hash(key)
        if self.table[hash_index] is not None:
            for pair in self.table[hash_index]:
                if pair[0] == key:
                    return pair[1]
        return None

a = HashTable()
a.set(11, 'apple')

a.set(1,"orange")
print(a.get(11))
print(a.get(1))
print(a.table)
