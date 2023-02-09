def solution(s):
    # cnt = 이진 변환의 횟수
    # cnt_0 = 변환 과정에서 제거된 모든 0의 개수
    cnt, cnt_0 = 0, 0 
    while s != '1':
        cnt_0 += s.count('0')
        temp = s.count('1')
        s = bin(temp)[2:] # 이진 변환
        cnt += 1
    return [cnt, cnt_0]