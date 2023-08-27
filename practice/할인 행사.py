from collections import Counter
def solution(want, number, discount):
    answer = 0
    
    check = {}
    
    for k,v in zip(want, number):
        check[k] = v
    
    for i in range(len(discount)-9):
        temp = Counter(discount[i:i+10])
        if temp == check:
            answer += 1
    
    return answer