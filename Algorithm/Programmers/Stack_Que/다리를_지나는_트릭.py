from collections import deque
from functools import reduce


def solution(bridge_length, weight, truck_weights):
    bridge = deque([])
    exit = []
    truck_weights = deque(truck_weights)
    truck_weights_length = len(truck_weights)
    elapsed_time = 0
    while len(exit) != truck_weights_length:

        # 다리 위의 트럭들의 무게의 합이 weight보다 작을 경우만 append 가능
        current_bridge_weight = (
            reduce(lambda x, y: x + y, [e[0] for e in bridge])
            if len(bridge) != 0
            else 0
        )
        truck_weight = truck_weights[0] if len(truck_weights) != 0 else weight + 1
        if (weight - current_bridge_weight) >= truck_weight and len(
            bridge
        ) < bridge_length:
            # truck_weight = truck_weights.popleft()  # 대기 트럭 리스트에서 pop
            bridge.append([truck_weights.popleft(), 0])  # 다리에 트럭을 둬야함

        # bridge_length의 크기만큼 다리위에 있었던 트럭은 pop되어 exit 리스트에 append 된다.
        if bridge[0][1] >= bridge_length:
            exit.append(bridge.popleft())
            current_bridge_weight = (
                reduce(lambda x, y: x + y, [e[0] for e in bridge])
                if len(bridge) != 0
                else 0
            )
            truck_weight = truck_weights[0] if len(truck_weights) != 0 else weight + 1
            if (weight - current_bridge_weight) >= truck_weight and len(
                bridge
            ) < bridge_length:
                # truck_weight = truck_weights.popleft()  # 대기 트럭 리스트에서 pop
                bridge.append([truck_weights.popleft(), 0])  # 다리에 트럭을 둬야함
        for truck in bridge:
            truck[1] += 1
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

    # bridge_length = 5
    # weight = 5
    # truck_weights = [2, 2, 2, 2, 1, 1, 1, 1, 1]
    print(solution(bridge_length, weight, truck_weights))


if __name__ == "__main__":
    main()
