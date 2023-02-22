from itertools import permutations
def solution(k, dungeons):
    length = len(dungeons)
    answer = 0
    lst = [per for per in permutations(dungeons,length)]
    for per in permutations(dungeons,length):
        temp_k = k
        count = 0
        for p in per:
            if temp_k >= p[0]:
                temp_k -= p[1]
                count += 1
        answer = max(answer, count)        
    return answer