def solution(t, p):
    answer = 0

    for i in range(len(t)):
        tmp = t[i:i + len(p)]
        if len(tmp) < len(p):
            break
        else:
            if int(tmp) <= int(p):
                answer += 1  
        
    return answer

def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1
    return answer