def solution(a, b, n):
    answer = 0 # 받은 콜라의 병 합계
    
    tmp = 0
    while n >= a:
        if n % a != 0:
            n -= 1
            tmp += 1 
        else:
            answer += (n // a) * b # 당시 받은 콜라의 병 수
            n = tmp + (n // a) * b # 현재 보유하고 있는 콜라의 병 수
            tmp = 0
        
    return answer


def solution(a, b, n):
    answer = 0

    while n >= a:
        remain = n % a # 남은 병 수
        answer += (n // a) * b # 받은 병 수
        n = remain + (n // a) * b # 받고 남은 거까지 더함
        
    return answer