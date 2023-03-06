# https://school.programmers.co.kr/learn/courses/30/lessons/154538?language=python3
from collections import deque

def solution(x, y, n):
    dp = [0] * 1000001
    
    q = deque()
    q.append(x)
    
    while q:
        x = q.popleft()
        if x == y:
            return dp[x]
        for nx in (x+n, x*2, x*3):
            if 0 <= nx <= 1000000 and dp[nx] == 0:
                dp[nx] = dp[x] + 1
                q.append(nx)

    return -1