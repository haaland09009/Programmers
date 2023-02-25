from collections import Counter
def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
        
    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]): 
            answer += 1
   

    return answer


#---------------------------------
# 직접 해결한 풀이
from collections import Counter
def solution(want, number, discount):
    answer = 0
    
    dic = {}
    for i,j in zip(want, number):
        dic[i] = j
        
    for i in range(len(discount)):
        tmp = Counter(discount[i:i+10])
        count = 0
        for k,v in dic.items():
            if dic[k] <= tmp[k]: 
                count += 1
        if count == len(want):
            answer += 1
 
    return answer