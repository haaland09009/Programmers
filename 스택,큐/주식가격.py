from collections import deque
def solution(prices):
    answer = []
    
    q = deque(prices)
    while q:
        now = q.popleft()
        time = 0
        for price in q:
            time += 1
            if now > price:
                break
        answer.append(time)        
   
    
    return answer
# --------------------------------------
# 직접 해결한 풀이
# def solution(prices):
#     answer = []
    
#     for i in range(len(prices)):
#         time = 0
#         for j in range(i+1, len(prices)):
#             time += 1
#             if prices[i] > prices[j]:
#                 break
#         answer.append(time)        
                
        
#     return answer