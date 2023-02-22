def is_prime(x): # 소수 진위 여부 판별
    if x <= 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: #  2 이상인 수 중에서 나누어 떨어지는 것이 하나라도 존재한다면
            return False # 소수가 아님.
    return True   

def k_num(n, k): # 진수 변환 사용자 정의 함수
    if k == 10: # 10진수라면 그대로 출력
        return n
    else: 
        new_n = ''
        while n > 0:
            new_n = str(n % k) + new_n
            n = n // k
        return new_n    
            
def solution(n, k):
    answer = 0
    num = k_num(n, k) # 위 함수 실행
    nums = str(num).split('0') # 출력된 수를 문자로 변환하여 0 기준으로 구분
    for x in nums:
        if x and is_prime(int(x)): # 소수일 경우
            answer += 1
    return answer

#---------------------------------------------------
def is_prime_number(x): #  소수 판별 함수
   if x <= 1:
       return False
   for i in range(2, int(x**0.5)+1): #  2 이상인 수 중에서 나누어 떨어지는 것이 하나라도 존재한다면
       if x % i == 0:
           return False
   return True

def k_num(n, k):
   tmp = ''
   while n > 0:
       tmp += str(n % k)
       n = n // k 
   return tmp[::-1]   
       

def solution(n, k):
   answer = 0
   result = k_num(n,k)
   ls = []
   for i in result.split('0'):
       ls.append(i)
   for i in ls:
       if i == '':
           continue
       else:
           if is_prime_number(int(i)):
               answer += 1
   return answer