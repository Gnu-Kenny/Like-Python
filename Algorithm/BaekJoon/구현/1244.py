import sys
input = sys.stdin.readline


class Student:
    def __init__(self, s, n):
        self.s = s  # 성별
        self.n = n  # 받은 수


def main():
    n = int(input())
    switches = [0] + list(map(int, input().split()))
    students = []
    for _ in range(int(input())):
        sex, num = list(map(int, input().split()))
        students.append(Student(sex, num))
    for stu in students:
        # 남학생 스위치 변경 알고리즘
        i = 1
        while stu.s == 1 and i <= n:
            switch_num = stu.n * i
            if switch_num > n:
                break
            if switches[switch_num] == 0:
                switches[switch_num] = 1
            else:
                switches[switch_num] = 0
            i += 1

        # 여학생 스위치 변경 알고리즘
        i = 1
        while stu.s == 2:
            if i == 1:
                if switches[stu.n] == 0:
                    switches[stu.n] = 1
                else:
                    switches[stu.n] = 0

            if stu.n + i > n or stu.n - i <= 0:
                break
            if switches[stu.n + i] == switches[stu.n - i]:
                if switches[stu.n + i] == 0:
                    switches[stu.n + i] = 1
                    switches[stu.n - i] = 1
                elif switches[stu.n + i] == 1:
                    switches[stu.n + i] = 0
                    switches[stu.n - i] = 0
            else:
                break
            i += 1
    switches.pop(0)
    for i in range(0, len(switches), 20):
        start_idx = i
        end_idx = i + 20
        if end_idx > len(switches):
            partial_switches = switches[start_idx:]
            print(*partial_switches)
        else:
            partial_switches = switches[start_idx:end_idx]
            print(*partial_switches)


if __name__ == "__main__":
    main()
