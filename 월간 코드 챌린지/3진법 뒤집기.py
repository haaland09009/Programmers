def solution(n):
    answer = 0
    tmp = ''
    while n != 0:
        tmp += str(n % 3)
        n = n // 3
    
    for i in range(len(tmp)):
        answer += (int(tmp[i]) * 3**(len(tmp)-1-i))

    return answer