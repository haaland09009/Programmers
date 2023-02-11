from itertools import combinations
def is_prime_number(x): # 소수 판별 함수
    if x <= 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True    

def solution(nums):
    answer = 0
    arr = [sum(com) for com in combinations(nums, 3)]
    for i in arr:
        if is_prime_number(i): # 소수일 경우
            answer += 1   
    return answer