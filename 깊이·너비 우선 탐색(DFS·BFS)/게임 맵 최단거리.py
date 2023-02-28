# https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3
from collections import deque
def solution(maps):
    answer = 0
    # 적은 게임 맵의 우측 하단에 위치 (문제에서 주어진 maps 배열에 따라 적의 좌표가 달라진다.)
    target_x, target_y = len(maps)-1, len(maps[-1])-1
    # 동서남북 방향 이동
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    q = deque()
    q.append((0,0)) # 캐릭터는 처음에 좌측 상단에 있으므로 (0,0)에서 시작
    while q: # queue가 실행되는 동안 ~~ (queue while문이 완전히 끝나면 더 이상 가야할 칸이 없는 것이다.)
        x,y = q.popleft() # 현재 좌표 꺼내기
        if x == target_x and y == target_y: # 만약 적의 좌표(목표 지점)에 도착한 것이라면
            answer = maps[target_x][target_y]
            break  
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[-1]): # 범위를 벗어날 경우
                continue
            if maps[nx][ny] == 1: # 갈 수 있는 길(흰색 부분)이라면
                maps[nx][ny] = maps[x][y] + 1 # 현재 꺼낸 좌표에 1 더하기
                q.append((nx,ny))
                
    if maps[target_x][target_y] == 1: # 적 진영에 도착하지 못할 경우 적의 좌표 값은 1로 변함이 없다.
        return -1
    else: # 적 진영에 도착했을 경우 지나온 칸 출력
        return answer