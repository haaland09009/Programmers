def solution(s, n):
    ls_lower = list('abcdefghijklmnopqrstuvwxyz'*2)
    ls_upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'*2)
    
    answer = ''
    for i in s:
        if i in ls_lower:
            answer += ls_lower[ls_lower.index(i) + n]
        elif i in ls_upper:    
            answer += ls_upper[ls_upper.index(i) + n]
        elif i == ' ':
            answer += ' '

    return answer