def solution(m, n, board):
    answer = 0
    
    b = []
    for i in board:
        b.append(list(i))
        
    # 주어진 board 배열을 한 번만 도는 것이 아니라 지워지는 블록이 없어질때까지 반복해야 하므로 while 반복문을 사용한다.    
    while True:
        rm = []
        for i in range(m-1):
            for j in range(n-1):
                if b[i][j] == b[i][j+1] and b[i][j+1] == b[i+1][j+1] and b[i+1][j] == b[i+1][j+1] and b[i][j] != 0:
                    rm.append((i,j))
                    rm.append((i,j+1))
                    rm.append((i+1,j))
                    rm.append((i+1,j+1))
        rm = set(rm) # 중복된 좌표는 제거해야 하므로 set 사용
        answer += len(rm) # 지워지는 블록의 좌표 수
        if len(rm) == 0: # 모든 좌표 확인 후 더 이상 지워지는 블록이 없다면 그동안 지워진 총 블록의 수를 출력한다.
            return answer
        else:
            for r in rm: # 지워지는 블록의 좌표는 0으로 처리한다.
                b[r[0]][r[1]] = 0
        
        # 지워진 블록의 좌표가 0으로 변경됨 -> 블록에 빈 공간이 생김. -> 위에 블록이 있으면아래로 떨어져 빈 공간을 채워야 한다.
        while True:
            mv = False # 블록의 이동 여부
            for i in range(m-1):
                for j in range(n):
                    if b[i][j] and b[i+1][j] == 0: # 현재 블록이 채워져있고 바로 아래에 있는 블록이 비워져 있을 경우
                        b[i+1][j] = b[i][j] # 빈 공간을 채운다.
                        b[i][j]  = 0 # 현재 좌표는 밑에 있는 빈 공간을 채워주었으므로 현재 블록 좌표는 비워지게 된다. (0으로 변경됨.)
                        mv = True
                    else:
                        continue
            if mv == False: # 이동해야 하는 블록이 1개도 없다면 while 반복문을 종료한다.
                break
        
    return answer