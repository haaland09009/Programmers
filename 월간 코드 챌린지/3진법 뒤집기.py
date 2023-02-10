def solution(n):
    answer = 0
    tmp = ''
    while n != 0:
        tmp += str(n % 3)
        n = n // 3
    
    for i in range(len(tmp)):
        answer += (int(tmp[i]) * 3**(len(tmp)-1-i))

    return answer

-------------------------------------------------------

def solution(n):
    answer = 0
    tmp = ''
    while n != 0:
        tmp += str(n % 3)
        n = n // 3

    return int(tmp, 3)

# int(x,3) : 3진법으로 구성된 x를 10진법으로 바꿔주는 역할을 한다.
