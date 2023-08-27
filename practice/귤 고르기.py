# 내가 푼 풀이
def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    
    dic = {}
    
    for t in tangerine:
        if t not in dic:
            dic[t] = 1
        else:
            dic[t] += 1
            
    for key, value in sorted(dic.items(), key=lambda x : x[1], reverse=True):
         k -= value
         answer += 1
         if k <= 0:
            break
    
    return answer


# 참고 풀이
import collections
def solution(k, tangerine):
    answer = 0
    
    cnt = collections.Counter(tangerine)
    
    for v in sorted(cnt.values(), reverse=True):
        k -= v
        answer += 1
        if k <= 0:
            break
    
    
    return answer    