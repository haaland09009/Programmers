def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        sum_value = 0
        for j in range(1, i+1):
            if i % j == 0: # 약수의 개수 구하기
                sum_value += 1 
        if sum_value % 2 == 0: # 약수의 개수가 짝수일 경우
            answer += i
        else: # 약수의 개수가 홀수일 경우
            answer -= i
            
    return answer