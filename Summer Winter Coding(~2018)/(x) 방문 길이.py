def solution(dirs):
    roads = set()
    d = {'L':(-1,0), 'R':(1,0), 'U':(0,1), 'D':(0,-1)}
    x,y = 0,0
    
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            roads.add((x,y,nx,ny))
            roads.add((nx,ny,x,y))
            x, y = nx, ny
            
        
    return len(roads) // 2