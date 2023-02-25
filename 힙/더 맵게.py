import heapq as hq
def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    
    while scoville[0] < K:
        first = hq.heappop(scoville)
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second * 2)
        answer += 1
        if len(scoville) <= 1 and scoville[0] < K:
            return -1

    return answer