def solution(n):
    cnt = 0
    for i in range(1, n+1):
        sum_val = i
        for j in range(i+1, n+1):
            sum_val += j
            if sum_val == n:
                cnt += 1
                break
            if sum_val > n:
                break
    return cnt + 1 # 자기 자신도 포함이므로 1을 더해준다.