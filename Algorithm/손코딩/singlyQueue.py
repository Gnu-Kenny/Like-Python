class Node():
    def __init__(self, value: int):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self._head = Node(0)
        self._last = self._head

    def enqueue(self, value: int):
        new_node = Node(value)
        self._last.next = new_node
        self._last = new_node

    def dequeue(self):
        if self._head == self._last:
            raise RuntimeError("Not found")

        first_node: Node = self._head.next

        value = first_node.value
        if first_node == self._last:
            self._head = self._last  # 큐가 빈 상태
            return value

        self._head.next = first_node.next
        return value


queue = Queue()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(7)
queue.enqueue(9)

print(queue.dequeue(), end=' ')
print(queue.dequeue(), end=' ')
print(queue.dequeue(), end=' ')
print(queue.dequeue(), end=' ')
print(queue.dequeue())
