class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def SizeOfList(self):
        return self._size

    def _get_node(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        cur = self.head
        i = 0
        while i < index:
            cur = cur.next
            i += 1
        return cur

    def InsertAtBegin(self, data):
        node = SNode(data)
        node.next = self.head
        self.head = node
        self._size += 1

    def InsertAtEnd(self, data):
        if self.head is None:
            self.InsertAtBegin(data)
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = SNode(data)
        self._size += 1

    def InsertAtIndex(self, data, index):
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
        if index == 0:
            self.InsertAtBegin(data)
            return
        prev = self._get_node(index - 1)
        node = SNode(data)
        node.next = prev.next
        prev.next = node
        self._size += 1

    def UpdateNode(self, data, index):
        node = self._get_node(index)
        node.data = data

    def RemoveNodeAtBegin(self):
        if self.head is None:
            raise IndexError("List is empty")
        val = self.head.data
        self.head = self.head.next
        self._size -= 1
        return val

    def RemoveNodeAtEnd(self):
        if self.head is None:
            raise IndexError("List is empty")
        if self.head.next is None:
            return self.RemoveNodeAtBegin()
        prev = self.head
        cur = self.head.next
        while cur.next is not None:
            prev = cur
            cur = cur.next
        val = cur.data
        prev.next = None
        self._size -= 1
        return val

    def RemoveNodeAtIndex(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        if index == 0:
            return self.RemoveNodeAtBegin()
        prev = self._get_node(index - 1)
        val = prev.next.data
        prev.next = prev.next.next
        self._size -= 1
        return val

    def Concatenate(self, other):
        cur = other.head
        while cur is not None:
            self.InsertAtEnd(cur.data)
            cur = cur.next

    def Invert(self):
        prev = None
        cur = self.head
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev


class CircularSinglyLinkedList:
    
    def __init__(self):
        self.tail = None
        self._size = 0

    def SizeOfList(self):
        return self._size

    def _head(self):
        if self.tail is None:
            return None
        return self.tail.next

    def InsertAtBegin(self, data):
        node = SNode(data)
        if self.tail is None:
            node.next = node
            self.tail = node
        else:
            node.next = self.tail.next
            self.tail.next = node
        self._size += 1

    def InsertAtEnd(self, data):
        self.InsertAtBegin(data)
        self.tail = self.tail.next

    def _get_node(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        cur = self._head()
        i = 0
        while i < index:
            cur = cur.next
            i += 1
        return cur

    def InsertAtIndex(self, data, index):
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
        if index == 0:
            self.InsertAtBegin(data)
            return
        if index == self._size:
            self.InsertAtEnd(data)
            return
        prev = self._get_node(index - 1)
        node = SNode(data)
        node.next = prev.next
        prev.next = node
        self._size += 1

    def UpdateNode(self, data, index):
        self._get_node(index).data = data

    def RemoveNodeAtBegin(self):
        if self.tail is None:
            raise IndexError("List is empty")
        head = self.tail.next
        val = head.data
        if self._size == 1:
            self.tail = None
        else:
            self.tail.next = head.next
        self._size -= 1
        return val

    def RemoveNodeAtEnd(self):
        if self.tail is None:
            raise IndexError("List is empty")
        if self._size == 1:
            return self.RemoveNodeAtBegin()
        cur = self.tail.next
        while cur.next is not self.tail:
            cur = cur.next
        val = self.tail.data
        cur.next = self.tail.next
        self.tail = cur
        self._size -= 1
        return val

    def RemoveNodeAtIndex(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        if index == 0:
            return self.RemoveNodeAtBegin()
        if index == self._size - 1:
            return self.RemoveNodeAtEnd()
        prev = self._get_node(index - 1)
        val = prev.next.data
        prev.next = prev.next.next
        self._size -= 1
        return val

    def Concatenate(self, other):
        cur = other._head()
        i = 0
        while i < other._size:
            self.InsertAtEnd(cur.data)
            cur = cur.next
            i += 1

    def Invert(self):
        if self._size <= 1:
            return
        head = self._head()
        self.tail.next = None  
        prev = None
        cur = head
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        new_head = prev
        new_tail = new_head
        while new_tail.next is not None:
            new_tail = new_tail.next
        new_tail.next = new_head
        self.tail = new_tail


class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def SizeOfList(self):
        return self._size

    def _get_node(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        if index < self._size // 2:
            cur = self.head
            i = 0
            while i < index:
                cur = cur.next
                i += 1
            return cur
        cur = self.tail
        i = self._size - 1
        while i > index:
            cur = cur.prev
            i -= 1
        return cur

    def InsertAtBegin(self, data):
        node = DNode(data)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node
        self._size += 1

    def InsertAtEnd(self, data):
        node = DNode(data)
        node.prev = self.tail
        if self.tail is not None:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self._size += 1

    def InsertAtIndex(self, data, index):
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
        if index == 0:
            self.InsertAtBegin(data)
            return
        if index == self._size:
            self.InsertAtEnd(data)
            return
        nxt = self._get_node(index)
        prv = nxt.prev
        node = DNode(data)
        node.prev = prv
        node.next = nxt
        prv.next = node
        nxt.prev = node
        self._size += 1

    def UpdateNode(self, data, index):
        self._get_node(index).data = data

    def RemoveNodeAtBegin(self):
        if self.head is None:
            raise IndexError("List is empty")
        val = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self._size -= 1
        return val

    def RemoveNodeAtEnd(self):
        if self.tail is None:
            raise IndexError("List is empty")
        val = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self._size -= 1
        return val

    def RemoveNodeAtIndex(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        if index == 0:
            return self.RemoveNodeAtBegin()
        if index == self._size - 1:
            return self.RemoveNodeAtEnd()
        node = self._get_node(index)
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        return node.data

    def Concatenate(self, other):
        cur = other.head
        while cur is not None:
            self.InsertAtEnd(cur.data)
            cur = cur.next

    def Invert(self):
        cur = self.head
        while cur is not None:
            tmp = cur.next
            cur.next = cur.prev
            cur.prev = tmp
            cur = tmp
        tmp = self.head
        self.head = self.tail
        self.tail = tmp



class LinkedListArray:
    def __init__(self):
        self._list = SinglyLinkedList()

    def Insert(self, obj, index):
        self._list.InsertAtIndex(obj, index)

    def Delete(self, index):
        return self._list.RemoveNodeAtIndex(index)

    def Find(self, obj):
        cur = self._list.head
        i = 0
        while cur is not None:
            if cur.data == obj:
                return i
            cur = cur.next
            i += 1
        return -1

    def get(self, index):
        return self._list._get_node(index).data

    def set(self, index, value):
        self._list.UpdateNode(value, index)



class LinkedListQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def IsEmpty(self):
        return self._size == 0

    def Enqueue(self, x):
        node = SNode(x)
        if self._tail is None:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def Dequeue(self):
        if self._head is None:
            raise IndexError("Queue is empty")
        val = self._head.data
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return val

    def Peek(self):
        if self._head is None:
            raise IndexError("Queue is empty")
        return self._head.data



class LinkedListStack:
    def __init__(self):
        self._head = None
        self._size = 0

    def IsEmpty(self):
        return self._size == 0

    def Push(self, x):
        node = SNode(x)
        node.next = self._head
        self._head = node
        self._size += 1

    def Pop(self):
        if self._head is None:
            raise IndexError("Stack is empty")
        val = self._head.data
        self._head = self._head.next
        self._size -= 1
        return val

    def Peek(self):
        if self._head is None:
            raise IndexError("Stack is empty")
        return self._head.data


if __name__ == "__main__":
    s = SinglyLinkedList()
    s.InsertAtEnd(1)
    s.InsertAtEnd(2)
    s.InsertAtEnd(3)
    s.Invert()
    print("Singly inverted head:", s.head.data)
