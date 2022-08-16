

from collections import defaultdict

# "car" == "cra"
# "car" != "carr"


def solution(string1: str, string2: str):
    hashmap = defaultdict(int)
    is_anagram = True

    for i in string1:
        hashmap[i] += 1

    map_keys = list(hashmap.keys())

    for i in string2:
        if i not in map_keys:
            is_anagram = False
            break

        if hashmap[i] == 0:
            is_anagram = False
            break

        hashmap[i] -= 1

    return is_anagram


def main():
    string1 = "carr"
    string2 = "car"
    print(solution(string1, string2))


if __name__ == "__main__":
    main()
