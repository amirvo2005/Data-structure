class DynamicArray:
    def __init__(self, capacity=4):
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

    def set(self, i, v):
        if i < 0 or i >= self._size:
            raise IndexError("Index out of range")
        self._data[i] = v

    def _resize(self, new_cap):
        new_data = [None] * new_cap
        i = 0
        while i < self._size:
            new_data[i] = self._data[i]
            i += 1
        self._data = new_data
        self._cap = new_cap

    def push_back(self, v):
        if self._size >= self._cap:
            self._resize(self._cap * 2)
        self._data[self._size] = v
        self._size += 1

    def delete_last(self):
        if self._size == 0:
            raise IndexError("Empty")
        val = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return val


class CircularQueue:
    def __init__(self, capacity):
        if capacity < 1:
            capacity = 1
        self._data = [None] * capacity
        self._cap = capacity
        self._front = 0
        self._size = 0

    def IsEmpty(self):
        return self._size == 0

    def IsFull(self):
        return self._size == self._cap

    def Enqueue(self, x):
        if self.IsFull():
            raise OverflowError("Queue is full")
        rear = (self._front + self._size) % self._cap
        self._data[rear] = x
        self._size += 1

    def Dequeue(self):
        if self.IsEmpty():
            raise IndexError("Queue is empty")
        val = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._cap
        self._size -= 1
        return val


class Graph:
    def __init__(self):
        self._verts = DynamicArray(4)
        self._adj = []  
        self._n = 0

    def _index_of(self, v):
        i = 0
        while i < self._n:
            if self._verts.get(i) == v:
                return i
            i += 1
        return -1

    def AddVertex(self, v):
        if self._index_of(v) != -1:
            return
        self._verts.push_back(v)
        old_n = self._n
        self._n += 1

        new_adj = [None] * self._n
        i = 0
        while i < self._n:
            new_adj[i] = [0] * self._n
            i += 1

        i = 0
        while i < old_n:
            j = 0
            while j < old_n:
                new_adj[i][j] = self._adj[i][j]
                j += 1
            i += 1
        self._adj = new_adj

    def AddEdge(self, a, b):
        self.AddVertex(a)
        self.AddVertex(b)
        ia = self._index_of(a)
        ib = self._index_of(b)
        self._adj[ia][ib] = 1
        self._adj[ib][ia] = 1

    def RemoveEdge(self, a, b):
        ia = self._index_of(a)
        ib = self._index_of(b)
        if ia == -1 or ib == -1:
            return
        self._adj[ia][ib] = 0
        self._adj[ib][ia] = 0

    def RemoveVertex(self, v):
        idx = self._index_of(v)
        if idx == -1:
            return
        old_n = self._n

        
        i = idx
        while i < self._n - 1:
            self._verts.set(i, self._verts.get(i + 1))
            i += 1
        self._verts.delete_last()

        self._n -= 1

        new_adj = [None] * self._n
        i = 0
        while i < self._n:
            new_adj[i] = [0] * self._n
            i += 1

        ni = 0
        oi = 0
        while oi < old_n:
            if oi == idx:
                oi += 1
                continue
            nj = 0
            oj = 0
            while oj < old_n:
                if oj == idx:
                    oj += 1
                    continue
                new_adj[ni][nj] = self._adj[oi][oj]
                nj += 1
                oj += 1
            ni += 1
            oi += 1

        self._adj = new_adj

    def BFS(self, start=None):
        if self._n == 0:
            return ""
        if start is None:
            s = 0
        else:
            s = self._index_of(start)
            if s == -1:
                return ""

        visited = [0] * self._n
        q = CircularQueue(self._n)
        visited[s] = 1
        q.Enqueue(s)

        order = DynamicArray(self._n)

        while not q.IsEmpty():
            v = q.Dequeue()
            order.push_back(self._verts.get(v))

            nb = 0
            while nb < self._n:
                if self._adj[v][nb] == 1 and visited[nb] == 0:
                    visited[nb] = 1
                    q.Enqueue(nb)
                nb += 1

        
        out = ""
        i = 0
        while i < order.size():
            if i != 0:
                out += " "
            out += str(order.get(i))
            i += 1
        return out

    def DFS(self, start=None):
        if self._n == 0:
            return ""
        if start is None:
            s = 0
        else:
            s = self._index_of(start)
            if s == -1:
                return ""

        visited = [0] * self._n
        order = DynamicArray(self._n)

        def dfs(i):
            visited[i] = 1
            order.push_back(self._verts.get(i))
            nb = 0
            while nb < self._n:
                if self._adj[i][nb] == 1 and visited[nb] == 0:
                    dfs(nb)
                nb += 1

        dfs(s)

        out = ""
        i = 0
        while i < order.size():
            if i != 0:
                out += " "
            out += str(order.get(i))
            i += 1
        return out


if __name__ == "__main__":
    g = Graph()
    g.AddEdge("A", "B")
    g.AddEdge("A", "C")
    g.AddEdge("B", "D")
    print("BFS:", g.BFS("A"))
    print("DFS:", g.DFS("A"))
