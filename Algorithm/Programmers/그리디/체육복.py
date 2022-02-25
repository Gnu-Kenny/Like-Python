def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = n - len(lost)
    lost_new = []
    for student in lost:
        if student in reserve:
            answer += 1
            
            reserve.pop(reserve.index(student))
            continue
        lost_new.append(student)
            
    for student in lost_new:
        if student - 1 in reserve:
            reserve.pop(reserve.index(student-1))
            answer += 1
            continue
        
        if student + 1 in reserve:
            answer += 1
            reserve.pop(reserve.index(student+1))
            
    return answer