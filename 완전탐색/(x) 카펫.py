def solution(brown, yellow):
    answer = []
    sum_value = brown + yellow
    
    for i in range(1, sum_value+1):
        if sum_value % i != 0:
            continue
        j = sum_value // i
        if (i-2) * (j-2) == yellow:
            return sorted([i,j], reverse=True)