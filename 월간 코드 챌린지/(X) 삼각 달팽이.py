# https://school.programmers.co.kr/learn/courses/30/lessons/68645
def solution(n):
    arr = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    cnt = 1

    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            arr[x][y] = cnt 
            cnt += 1

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                answer.append(arr[i][j])
    return answer