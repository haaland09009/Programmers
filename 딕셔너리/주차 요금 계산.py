import math
def solution(fees, records):
    dic = {}

    for r in records:
        time = r.split(' ')[0]
        car_number = r.split(' ')[1]
        if car_number not in dic:
            dic[car_number] = [time]
        else:
            dic[car_number].append(time)
    
    answer = []
    for k,v in sorted(dic.items()):
        total_time = 0 # 각 차량의 누적 주차 시간을 담을 변수
        if len(v) % 2 != 0: # 입차 이후 출차 기록이 없다면 23:59에 출차된 것으로 간주
            dic[k].append('23:59')    
            
        for i in range(1, len(v), 2):
            hour = int(v[i].split(':')[0]) - int(v[i-1].split(':')[0])
            minute = int(v[i].split(':')[1]) - int(v[i-1].split(':')[1])
            total_time += hour * 60 + minute   
            
        if total_time <= fees[0]: # 각 차량의 누적 주차 시간이 기본 시간 이하일 경우
            answer.append(fees[1]) # 기본 요금으로 계산
        else:
            answer.append(fees[1] + math.ceil((total_time - fees[0]) / fees[2]) * fees[3])

    return answer