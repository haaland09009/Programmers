# https://school.programmers.co.kr/learn/courses/30/lessons/161989
from collections import deque
def solution(n, m , section):
    answer = 0				
    q = deque(section)	
  
    while q:
        start = q.popleft()	# 페인트칠 시작
        while q and start + m > q[0]: 
            q.popleft()
        answer += 1

    return answer
