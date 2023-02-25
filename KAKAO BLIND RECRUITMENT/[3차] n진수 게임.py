def convert(num, n): # 진수 변환 함수
    numbers = '0123456789ABCDEF'
    if num == 0: # 변환하려는 수가 0일 경우
        return '0'
    else:
        temp = ''
        while num > 0:
            temp = numbers[num % n] + temp
            num = num // n
        return temp    

def solution(n, t, m, p):
    tmp = ''  # 미리 구해야할 숫자
    answer = '' # 말해야 하는 숫자
    for i in range(t*m): 
        tmp += convert(i, n)
    for i in range(t): 
        answer += tmp[p-1 + i*m]
    return answer




#----------------------------------------
# 직접 해결한 풀이
def k_num(num, n): # num: 숫자, n: 진법
    numbers = '0123456789ABCDEF'
    tmp = ''
    while num > 0:
        tmp += numbers[num % n]
        num = num // n
    return tmp[::-1]
    

def solution(n, t, m, p):
    answer = '' # 말해야 하는 숫자
    temp = '' # 미리 구해야할 숫자
    for i in range(t*m):
        if i == 0:
            temp += '0'
        else:    
            temp += k_num(i, n)
    for i in range(p-1, t*m, m):
        answer += temp[i]
   
    return answer