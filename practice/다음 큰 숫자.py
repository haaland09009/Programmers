def solution(n):
    origin_n = n # 제시된 자연수 n 저장
    while True:
        n += 1 
        if bin(origin_n)[2:].count('1') == bin(n)[2:].count('1'):
            return n
            break