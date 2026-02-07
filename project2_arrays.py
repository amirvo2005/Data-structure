class DynamicArray:
    def __init__(self, capacity=4):
        if capacity < 1:
            capacity = 1
        self._cap = capacity
        self._size = 0
        self._data = [None] * self._cap

    def size(self):
        return self._size

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        return self._data[index]

    def set(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        self._data[index] = value

    def _resize(self, new_cap):
        new_data = [None] * new_cap
        i = 0
        while i < self._size:
            new_data[i] = self._data[i]
            i += 1
        self._data = new_data
        self._cap = new_cap

    def push_back(self, value):
        if self._size >= self._cap:
            self._resize(self._cap * 2)
        self._data[self._size] = value
        self._size += 1

    
    def Insert(self, obj, index):
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
        if self._size >= self._cap:
            self._resize(self._cap * 2)

        i = self._size
        while i > index:
            self._data[i] = self._data[i - 1]
            i -= 1
        self._data[index] = obj
        self._size += 1

    
    def Delete(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        removed = self._data[index]
        i = index
        while i < self._size - 1:
            self._data[i] = self._data[i + 1]
            i += 1
        self._data[self._size - 1] = None
        self._size -= 1

    
        if self._cap > 4 and self._size <= self._cap // 4:
            new_cap = self._cap // 2
            if new_cap < 4:
                new_cap = 4
            self._resize(new_cap)

        return removed

    
    def Find(self, obj):
        i = 0
        while i < self._size:
            if self._data[i] == obj:
                return i
            i += 1
        return -1


def sparse_matrix_of_square(matrix):
    
    n = len(matrix)
    
    i = 0
    while i < n:
        if len(matrix[i]) != n:
            raise ValueError("Matrix must be n x n")
        i += 1

    res = DynamicArray(8)
    i = 0
    while i < n:
        j = 0
        while j < n:
            v = matrix[i][j]
            if v != 0 and v is not None:
                res.push_back((i, j, v))
            j += 1
        i += 1

    out = [None] * res.size()
    k = 0
    while k < res.size():
        out[k] = res.get(k)
        k += 1
    return out


if __name__ == "__main__":
    arr = DynamicArray(2)
    arr.push_back(10)
    arr.push_back(20)
    arr.Insert(99, 1)
    print("Find 99:", arr.Find(99))
    print("Delete index 1:", arr.Delete(1))
    print("Now size:", arr.size())

    m = [
        [0, 0, 5],
        [0, 0, 0],
        [7, 0, 0]
    ]
    print("Sparse:", sparse_matrix_of_square(m))
