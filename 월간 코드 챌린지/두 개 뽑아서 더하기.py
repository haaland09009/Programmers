from itertools import combinations
def solution(numbers):
    answer = set()
    for arr in list(combinations(numbers, 2)):
        answer.add(sum(arr))
    
    return sorted(answer)