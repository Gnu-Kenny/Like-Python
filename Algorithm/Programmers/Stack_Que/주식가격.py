from collections import deque


def solution(prices):
    prices = deque(prices)
    answer = []
    prices_length = len(prices)
    while len(answer) != prices_length:
        if len(prices) == 0:
            break
        prev_price = prices.popleft()
        count = 0
        for price in prices:
            if prev_price <= price:  # 가격이 떨어지지 않았을때
                count += 1
            else:  # 가격이 떨어졌을때
                count += 1
                break

        answer.append(count)

    return answer


def main():
    prices = [1, 2, 3, 2, 3, 1]
    # prices = [4, 2, 3, 2, 3]
    print(solution(prices))


if __name__ == "__main__":
    main()
