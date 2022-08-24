import random


def main():
    check_number_list = [i for i in range(10 + 1)]
    random_number_list = [random.randint(1, 10) for _ in range(10)]
    print(random_number_list)
    for i, num in enumerate(random_number_list):
        if check_number_list[num] == 0:
            print(num, "is duplicate")
            return
        elif check_number_list[num] == random_number_list[i]:
            check_number_list[num] = 0
    print("is not duplicate")
    return


if __name__ == "__main__":
    main()
