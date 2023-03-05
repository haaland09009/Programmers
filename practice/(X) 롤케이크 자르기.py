# https://school.programmers.co.kr/learn/courses/30/lessons/132265

from collections import Counter
def solution(topping):
    answer = 0
    tp = Counter(topping)
    checked = set()
    
    for i in topping:
        tp[i] -= 1
        checked.add(i)
        if tp[i] == 0:
            tp.pop(i)
        if len(checked) == len(tp):
            answer += 1
    
    return answer