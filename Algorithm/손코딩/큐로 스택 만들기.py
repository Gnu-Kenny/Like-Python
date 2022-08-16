import queue


class Stack():
    def __init__(self):
        self.q = queue.Queue()

    def push(self, num: int):
        self.q.put(num)

    def pop(self):
        size = self.q.qsize()
        if size == 0:
            return -1
        for _ in range(size-1):
            self.q.put(self.q.get())
        # while self.q.qsize()
        return self.q.get()


def main():
    stack = Stack()

    stack.push(5)
    stack.push(6)
    stack.push(7)
    print(stack.pop())
    print(stack.pop())
    stack.push(1)
    print(stack.pop())


if __name__ == "__main__":
    main()
