from string import ascii_uppercase

def solution(name):
    uppercase = list(ascii_uppercase)
    right_move_count = 0
    left_move_count = 0
    word = ['A' for _ in range(len(name))]
    for i in range(len(name)):
        if name[i] == 'A':
            pass
        else:
            right_move_count += uppercase.index(name[i])
            word[i] = name[i]
        print(word)
        if word == list(name):
            break
        right_move_count += 1
    word = ['A' for _ in range(len(name))]
    for i in range(len(name)):
        if name[-i] == 'A':
            pass
        else:
            left_move_count += uppercase.index(name[-i])
            word[-i] = name[-i]
        print(word)
        if word == list(name):
            break
        left_move_count += 1
    
    word = ['A' for _ in range(len(name))]
    for i in range(len(name)):
        if name[-i] == 'A':
            pass
        else:
            left_move_count += uppercase.index(name[-i])
            word[-i] = name[-i]
        print(word)
        if word == list(name):
            break
        left_move_count += 1
    print(right_move_count-1)
    print(left_move_count-1)
    answer = min(right_move_count+1,left_move_count+1)
    return answer

def main():
    name = "JEROEN"
    # name = "JAN"
    print(solution(name))

if __name__ == "__main__":
    main()
# 오른쪽으로 탐색
# 왼쪽으로 탐색
# max(오, 왼)
# 