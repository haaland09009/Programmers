import heapq as hq
def solution(k, score):
    answer = []
    heap = []
    
    for i in score:
        hq.heappush(heap, i)
        if len(heap) > k: # 축적된 점수가 k개가 넘어갈 경우 힙에서 가장 작은 점수 제거
            hq.heappop(heap) 
        answer.append(heap[0]) # 힙에서 최하위 점수 추출    
    
    return answer