# https://school.programmers.co.kr/learn/courses/30/lessons/77885
def solution(numbers):
    answer = []
    for num in numbers: 
        if num % 2 == 0: # 짝수일 때
            answer.append(num+1)
        else: # 홀수일 때
            num = format(num,'b') # 2진수로 변환한다
            if not '0' in num: # 0이 하나도 없는 경우
                answer.append(int('10' + num[1:], 2))
            else: # 0이 있는 경우
                # rfind: 지정 문자열 마지막 위치 찾기
                index = num.rfind('0')
                answer.append(int(num[:index]+'10'+num[index+2:],2))
                
    return answer