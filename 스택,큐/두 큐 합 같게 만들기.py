# https://school.programmers.co.kr/learn/courses/30/lessons/118667?language=python3

from collections import deque
def solution(q1, q2):
    answer = 0
    tot1, tot2 = sum(q1), sum(q2)
    total = sum(q1) + sum(q2)
    q1, q2 = deque(q1), deque(q2)
    limit = len(q1) * 3
    
    while True:
        if tot1 > tot2:
            tmp = q1.popleft()
            q2.append(tmp)
            tot1 -= tmp
            tot2 += tmp
            answer += 1
        elif tot1 < tot2:
            tmp = q2.popleft()
            q1.append(tmp)
            tot1 += tmp
            tot2 -= tmp
            answer += 1
        else:
            break
        if answer == limit:
            return -1
    
    return answer