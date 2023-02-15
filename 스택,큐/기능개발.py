def solution(progresses, speeds):
    answer = []
    
    cnt = 0 # 기능 배포 수
    day = 1 
    while progresses:
        if progresses[0] + (speeds[0] * day) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else: # 각 기능이 100%에 못 미친다면
            if cnt > 0: # 배포되어야할 기능이 남아있을 때
                answer.append(cnt)
                day += 1
                cnt = 0
            else: # 배포되어야할 기능이 없을 때
                day += 1
 
    answer.append(cnt)  # 마지막 남은 기능의 배포 수               
            
    return answer