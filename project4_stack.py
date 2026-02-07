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

    def delete_last(self):
        if self._size == 0:
            raise IndexError("Empty")
        val = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return val


class Stack:
    def __init__(self):
        self._arr = DynamicArray(4)

    def IsEmpty(self):
        return self._arr.size() == 0

    def Push(self, x):
        self._arr.push_back(x)

    def Pop(self):
        if self.IsEmpty():
            raise IndexError("Stack is empty")
        return self._arr.delete_last()

    def Peek(self):
        if self.IsEmpty():
            raise IndexError("Stack is empty")
        return self._arr.get(self._arr.size() - 1)


class QueueUsingStacks:
    def __init__(self):
        self._in = Stack()
        self._out = Stack()

    def IsEmpty(self):
        return self._in.IsEmpty() and self._out.IsEmpty()

    def Enqueue(self, x):
        self._in.Push(x)

    def _move(self):
        while not self._in.IsEmpty():
            self._out.Push(self._in.Pop())

    def Dequeue(self):
        if self._out.IsEmpty():
            self._move()
        if self._out.IsEmpty():
            raise IndexError("Queue is empty")
        return self._out.Pop()

    def Peek(self):
        if self._out.IsEmpty():
            self._move()
        if self._out.IsEmpty():
            raise IndexError("Queue is empty")
        return self._out.Peek()


if __name__ == "__main__":
    q = QueueUsingStacks()
    q.Enqueue(1)
    q.Enqueue(2)
    print("Dequeue:", q.Dequeue())
    print("Peek:", q.Peek())
