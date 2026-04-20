def solution(bridge_length, weight, truck_weights):
    time = 0
    current_weight = 0
    bridge = [0] * bridge_length

    while len(bridge):
        time += 1

        # 빠지는 트럭값
        out = bridge.pop(0)
        current_weight -= out

        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
                current_weight += truck
            else:
                bridge.append(0)

    return time
