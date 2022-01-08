from collections import deque
from functools import reduce


def solution(bridge_length, weight, truck_weights):
    bridge = deque([])
    exit = []
    truck_weights = deque(truck_weights)
    elapsed_time = 0
    while len(truck_weights) != 0:
        # if len(bridge) == 0:
        #     truck_weight = truck_weights.popleft()
        # elif weight - reduce(lambda x, y: x + y, bridge) < truck_weights[0]:
        #     truck_weight = truck_weights.popleft()

        # 다리 위의 트럭들의 무게의 합이 weight보다 작을 경우만 append 가능
        current_bridge_weight = (
            reduce(lambda x, y: x + y, bridge) if len(bridge) != 0 else 0
        )
        if weight - current_bridge_weight >= truck_weights[0]:
            truck_weight = truck_weights.popleft() # 대기 트럭 리스트에서 pop
            bridge.append([truck_weight,0])  # 다리에 트럭을 둬야함
        
        # bridge_length의 크기만큼 다리위에 있었던 트럭은 pop되어 exit 리스트에 append 된다.
        for truck in range(len(bridge)):
            if truck[1] == weight:
                exit.append(truck[1])
            truck[1] += 1
        bridge.
        elapsed_time += 1

    return elapsed_time


def main():
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]
    # return 8

    bridge_length = 100
    weight = 100
    truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    # return 110
    solution(bridge_length, weight, truck_weights)


if __name__ == "__main__":
    main()
