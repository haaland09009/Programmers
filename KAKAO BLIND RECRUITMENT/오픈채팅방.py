def solution(record):
    answer = []
    
    dic = {}
    for r in record:  
        # 채팅방에 들어가거나 닉네임을 변경한 경우, 딕셔너리 key에 대한 value 값 설정 및 변경
        if r.split(' ')[0] == 'Enter' or r.split(' ')[0] == 'Change':
            dic[r.split(' ')[1]] = r.split(' ')[2]
    
    for r in record:
        # 채팅방에 들어가거나 나가는 경우에만 출력한다.
        if r.split(' ')[0] == 'Enter':
            answer.append(dic[r.split(' ')[1]] + "님이 들어왔습니다.")
        elif r.split(' ')[0] == 'Leave':
            answer.append(dic[r.split(' ')[1]] + "님이 나갔습니다.")
        
    return answer