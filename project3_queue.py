class ArrayQueue:
    
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("capacity must be >= 1")
        self._data = [None] * capacity
        self._cap = capacity
        self._size = 0

    def IsEmpty(self):
        return self._size == 0

    def IsFull(self):
        return self._size == self._cap

    def Enqueue(self, value):
        if self.IsFull():
            raise OverflowError("Queue is full")
        self._data[self._size] = value
        self._size += 1

    def Dequeue(self):
        if self.IsEmpty():
            raise IndexError("Queue is empty")
        val = self._data[0]
        i = 0
        while i < self._size - 1:
            self._data[i] = self._data[i + 1]
            i += 1
        self._data[self._size - 1] = None
        self._size -= 1
        return val

    def Peek(self):
        if self.IsEmpty():
            raise IndexError("Queue is empty")
        return self._data[0]

    def ReverseQueue(self):
        q = ArrayQueue(self._cap)
        i = self._size - 1
        while i >= 0:
            q.Enqueue(self._data[i])
            i -= 1
        return q


class CircularQueue:
    
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("capacity must be >= 1")
        self._data = [None] * capacity
        self._cap = capacity
        self._front = 0
        self._size = 0

    def IsEmpty(self):
        return self._size == 0

    def IsFull(self):
        return self._size == self._cap

    def Enqueue(self, value):
        if self.IsFull():
            raise OverflowError("Queue is full")
        rear = (self._front + self._size) % self._cap
        self._data[rear] = value
        self._size += 1

    def Dequeue(self):
        if self.IsEmpty():
            raise IndexError("Queue is empty")
        val = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._cap
        self._size -= 1
        return val

    def Peek(self):
        if self.IsEmpty():
            raise IndexError("Queue is empty")
        return self._data[self._front]

    def ReverseQueue(self):
        q = CircularQueue(self._cap)
        tmp = [None] * self._size
        i = 0
        while i < self._size:
            tmp[i] = self._data[(self._front + i) % self._cap]
            i += 1
        i = self._size - 1
        while i >= 0:
            q.Enqueue(tmp[i])
            i -= 1
        return q


if __name__ == "__main__":
    cq = CircularQueue(5)
    cq.Enqueue(10)
    cq.Enqueue(20)
    cq.Enqueue(30)
    print("Peek:", cq.Peek())
    print("Dequeue:", cq.Dequeue())
    rq = cq.ReverseQueue()
    print("Reverse Peek:", rq.Peek())
