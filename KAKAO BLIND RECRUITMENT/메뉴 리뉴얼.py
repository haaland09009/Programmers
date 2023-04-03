# https://school.programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for k in course:
        candidates = []
        for order in orders:
            for li in combinations(order, k):
                res = ''.join(sorted(li))
                candidates.append(res)
        result = Counter(candidates).most_common()
        answer += [menu for menu, count in result if count > 1 and count == result[0][1]]
            
    return sorted(answer)
