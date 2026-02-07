class DynamicArray:
    
    def __init__(self, capacity=8):
        if capacity < 1:
            capacity = 1
        self._cap = capacity
        self._size = 0
        self._data = [None] * self._cap

    def size(self):
        return self._size

    def get(self, i):
        if i < 0 or i >= self._size:
            raise IndexError("Index out of range")
        return self._data[i]

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


def recursive_power(a, b):
    
    if b < 0:
        raise ValueError("b must be non-negative")
    if b == 0:
        return 1
    if b == 1:
        return a
    half = recursive_power(a, b // 2)
    if b % 2 == 0:
        return half * half
    return half * half * a


def combination_recursive(n, r):
    
    if n < 0 or r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1
    return combination_recursive(n - 1, r - 1) + combination_recursive(n - 1, r)


def hanoi_of_tower(n, source="A", auxiliary="B", target="C"):
    
    moves = DynamicArray(8)

    def solve(k, s, a, t):
        if k == 0:
            return
        solve(k - 1, s, t, a)
        moves.push_back((s, t))
        solve(k - 1, a, s, t)

    if n < 0:
        raise ValueError("n must be >= 0")
    solve(n, source, auxiliary, target)

    
    out = [None] * moves.size()
    i = 0
    while i < moves.size():
        out[i] = moves.get(i)
        i += 1
    return out


if __name__ == "__main__":
    print("8^2 =", recursive_power(8, 2))
    print("C(5,2) =", combination_recursive(5, 2))
    print("Hanoi moves for n=3:")
    mv = hanoi_of_tower(3)
    i = 0
    while i < len(mv):
        print(mv[i])
        i += 1
