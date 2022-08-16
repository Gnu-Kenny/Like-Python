import sys
input = sys.stdin.readline


class Queue:
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def push(self, num: int):
        self.stack1.append(num)

    def pop(self):
        # stack2에 값이 없다면
        if len(self.stack2) == 0:
            # stack1의 모든 값을 pop하여 stack2에 채운다.
            while len(self.stack1) > 0:
                if len(self.stack1) > 0:
                    self.stack2.append(self.stack1.pop())

        if len(self.stack2) == 0:
            return -1
        return self.stack2.pop()

    def size(self):
        return len(self.stack1) + len(self.stack2)

    def empty(self):
        is_empty = 1
        if len(self.stack1) != 0 or len(self.stack2) != 0:
            is_empty = 0

        return is_empty

    def front(self):
        while len(self.stack1) > 0:
            if len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        if len(self.stack2) == 0:
            return -1
        return self.stack2[-1]

    def back(self):
        while len(self.stack1) > 0:
            if len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        if len(self.stack2) == 0:
            return -1
        return self.stack2[0]


def main():
    q = Queue()
    for _ in range(int(input())):
        command = input().strip().split(" ")
        if command[0] == 'push':
            q.push(int(command[1]))
        elif command[0] == 'pop':
            print(q.pop())
        elif command[0] == 'size':
            print(q.size())
        elif command[0] == 'front':
            print(q.front())
        elif command[0] == 'back':
            print(q.back())
        elif command[0] == 'empty':
            print(q.empty())


if __name__ == "__main__":
    main()
