def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        if len(score[i:i+m]) < m:
            continue
        else:
            min_value = min(score[i:i+m])
        answer += min_value * m
    return answer



def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i,v in enumerate(score):
        if (i+1) % m == 0:
            answer += v * m
    return answer    