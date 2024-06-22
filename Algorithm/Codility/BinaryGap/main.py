def solution(N):
    now_idx = 0
    past_idx = 0
    idx = 1
    binary_gap = 0
    max_binary_gap = 0
    
    while N >= 1:
        if N % 2 == 1:
            past_idx = now_idx
            now_idx = idx

            if now_idx > 0 and past_idx > 0:
                binary_gap = now_idx - past_idx - 1
                
                max_binary_gap = max(max_binary_gap, binary_gap)
        N = int(N/2)
        idx += 1

    return max_binary_gap