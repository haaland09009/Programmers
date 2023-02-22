word = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ') # 문자를 담은 리스트 생성
def solution(msg):
    answer = []
    start, end = 0,0
    while True:
        end += 1 
        if end == len(msg):
            answer.append(word.index(msg[start:end]))
            break
        if msg[start:end+1] not in word:
            word.append(msg[start:end+1])
            answer.append(word.index(msg[start:end]))
            start = end
    return answer   