import sys
input = sys.stdin.readline

k = 0
signs = []
max_v = 0
min_v = 9999999999
answer = []
visit = [0 for _ in range(0, 9+1)]
mx_v = ""
mn_v = ""


def back(level: int):
    global k, signs, max_v, min_v, answer, mx_v, mn_v

    if level == k+1:
        ans_str = "".join(list(map(str, answer)))
        if max_v < int(ans_str):
            max_v = int(ans_str)
            mx_v = ans_str
        if min_v > int(ans_str):
            min_v = int(ans_str)
            mn_v = ans_str
        return

    s = signs[level]

    for i in range(0, 9+1):
        if visit[i]:
            continue
        visit[i] = 1
        answer.append(i)
        if level > 0:
            # 각 부호의 반대 상황일때는 answer에 append하지 않는다.
            if s == ">":
                if answer[level] > answer[level-1]:
                    visit[i] = 0
                    answer.pop()
                    continue
            elif s == "<":
                if answer[level] < answer[level-1]:
                    visit[i] = 0
                    answer.pop()
                    continue
            else:
                pass

        back(level+1)
        visit[i] = 0
        answer.pop()


def main():
    global k, signs, max_v, min_v, answer, mx_v, mn_v

    k = int(input())
    signs = [0]
    signs += list(input().split())

    back(0)

    print(mx_v)
    print(mn_v)


if __name__ == "__main__":
    main()
