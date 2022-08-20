from collections import deque
from queue import SimpleQueue
import sys
input = sys.stdin.readline


class MaxQueue:
    def __init__(self):
        self._queue = SimpleQueue()
        self._max = deque()

    def enqueue(self, value):
        self._queue.put(value)

        if len(self._max) == 0:
            self._max.append(value)
            return

        while len(self._max) > 0 and value > self._max[-1]:
            self._max.pop()
        self._max.append(value)

    def dequeue(self):
        if self._queue.qsize() == 0:
            raise RuntimeError("queue is empty")

        value = self._queue.get()

        if value == self._max[0]:
            self._max.popleft()
        return value

    def getMax(self):
        if self._queue.qsize() == 0:
            raise RuntimeError("queue is empty")
        return self._max[0]

    def __str__(self):
        return "qsize = " + str(self._queue.qsize())


def main():

    max_queue = MaxQueue()
    max_queue.enqueue(1)
    max_queue.enqueue(3)
    max_queue.enqueue(5)
    print("max value =", max_queue.getMax())
    max_queue.enqueue(4)
    max_queue.dequeue()
    max_queue.dequeue()
    max_queue.dequeue()
    print("max value =", max_queue.getMax())
    max_queue.enqueue(7)

    print("max value =", max_queue.getMax())


if __name__ == "__main__":
    main()
