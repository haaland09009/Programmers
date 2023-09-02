# https://school.programmers.co.kr/learn/courses/30/lessons/42746
# 참고 : https://yuna0125.tistory.com/145
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))
