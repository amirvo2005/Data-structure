class HNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity=8):
        if capacity < 1:
            capacity = 1
        self._cap = capacity
        self._buckets = [None] * self._cap
        self._size = 0

    def HashFunction(self, key):
        
        if isinstance(key, int):
            if key < 0:
                key = -key
            return key % self._cap

        
        s = str(key)
        h = 0
        i = 0
        while i < len(s):
            h = (h * 31 + ord(s[i])) % self._cap
            i += 1
        return h

    def _rehash(self, new_cap):
        old_buckets = self._buckets
        old_cap = self._cap

        self._cap = new_cap
        self._buckets = [None] * self._cap
        self._size = 0

        i = 0
        while i < old_cap:
            node = old_buckets[i]
            while node is not None:
                self.Insert(node.key, node.value)
                node = node.next
            i += 1

    def Insert(self, key, value):
        idx = self.HashFunction(key)
        node = self._buckets[idx]
        while node is not None:
            if node.key == key:
                node.value = value
                return
            node = node.next

        new_node = HNode(key, value)
        new_node.next = self._buckets[idx]
        self._buckets[idx] = new_node
        self._size += 1

        
        if self._size * 4 >= self._cap * 3:
            self._rehash(self._cap * 2)

    def Search(self, key):
        idx = self.HashFunction(key)
        node = self._buckets[idx]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def Remove(self, key):
        idx = self.HashFunction(key)
        node = self._buckets[idx]
        prev = None
        while node is not None:
            if node.key == key:
                if prev is None:
                    self._buckets[idx] = node.next
                else:
                    prev.next = node.next
                self._size -= 1
                return node.value
            prev = node
            node = node.next
        return None


if __name__ == "__main__":
    ht = HashTable()
    ht.Insert("x", 100)
    ht.Insert("y", 200)
    print("Search x:", ht.Search("x"))
    print("Remove x:", ht.Remove("x"))
    print("Search x:", ht.Search("x"))
