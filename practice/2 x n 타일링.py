# https://school.programmers.co.kr/learn/courses/30/lessons/12900
def solution(n):
    # 규칙성을 발견하는 것으로 문제를 해결하였다.
    # n (가로의 길이)이 1일 때 만들 수 있는 경우의 수는 1, 2일 때 2, 3일 때 3
    # n이 4일 때 5, 즉 n = 3일 때부터 n-1 + n-2의 경우의 수를 더한 값이 나온다는 것을 유추하였다.
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[n]