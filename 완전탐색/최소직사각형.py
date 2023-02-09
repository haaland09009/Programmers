def solution(sizes):
    
    for i in range(1, len(sizes)):
        if max(sizes[i][0], sizes[i-1][0]) * max(sizes[i][1], sizes[i-1][1]) > max(sizes[i][1], sizes[i-1][0]) * max(sizes[i][0], sizes[i-1][1]):
            sizes[i][0], sizes[i][1] = max(sizes[i][1], sizes[i-1][0]), max(sizes[i][0], sizes[i-1][1])
        else:
            sizes[i][0], sizes[i][1] = max(sizes[i][0], sizes[i-1][0]), max(sizes[i][1], sizes[i-1][1])
 
    return sizes[-1][0] * sizes[-1][1]