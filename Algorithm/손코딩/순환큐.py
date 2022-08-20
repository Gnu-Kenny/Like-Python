

class CircularQueue:
    # 배열의 크기를 할당
    def __init__(self, k):
        self._data = [None] * k
        self._frontIdx = 0
        self._rearIdx = -1
        self._size = 0

    def enQueue(self, value):
        self._fullCheck()

        self._rearIdx += 1
        self._rearIdx = self._rearIdx % len(self._data)
        self._size += 1
        self._data[self._rearIdx] = value
        return self._data[self._frontIdx]

    def deQueue(self):
        self._emptyCheck()

        value = self._data[self._frontIdx]

        self._frontIdx += 1
        self._frontIdx = self._frontIdx % len(self._data)
        self._size -= 1

        return value

    def front(self):
        self._emptyCheck()
        return self._data[self._frontIdx]

    def rear(self):
        self._emptyCheck()
        return self._data[self._rearIdx]

    def _fullCheck(self):
        if self._size == len(self._data):
            raise RuntimeError("Queue is full")

    def _emptyCheck(self):
        if self._size == 0:
            raise RuntimeError("Queue is empty")


queue = CircularQueue(4)

queue.enQueue(3)
queue.enQueue(2)
queue.enQueue(1)
queue.enQueue(4)

print(queue.deQueue())

queue.enQueue(2)

print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())
