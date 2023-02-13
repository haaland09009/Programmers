def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1] # 순위

    cnt = 0 # 실제 당첨된 수
    for i in lottos:
        if i in win_nums:
            cnt += 1
    # 최고: 0도 당첨으로 가정하여 추가한다.
    high = lottos.count(0) + cnt 
    # 최저
    low = cnt 
            
    return [rank[high], rank[low]]