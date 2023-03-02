# https://school.programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations
def is_prime_number(x): # 소수 판별 함수
    result = True
    if x <= 1: 
        result = False
    for i in range(2, int(x**0.5)+1): 
        if x % i == 0:
            result = False
    return result        
        

def solution(numbers):
    answer = []
    numbers = list(map(str, numbers))
    for i in range(len(numbers)):
        for per in permutations(numbers, i+1):
            n = int(''.join(per))
            if is_prime_number(n) and int(n) not in answer:
                answer.append(n)
    return len(answer)