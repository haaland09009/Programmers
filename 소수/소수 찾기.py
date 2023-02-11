def is_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True    

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if is_prime_number(i):
            answer += 1
    return answer