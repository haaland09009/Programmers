def solution(land):
    answer = 0
    
    for i in range(1, len(land)):
        for j in range(len(land[i])):
            land[i][j] = land[i][j] + max(land[i -1][: j] + land[i - 1][j + 1:]) 
            
    return max(land[-1])

#----------------------------------------------------
# 직접 해결한 풀이
# def solution(land):
#     answer = 0
    
#     for i in range(1, len(land)):
#         for j in range(len(land[i])):
#             if j == 0:
#                 land[i][j] += max(land[i-1][j+1], land[i-1][j+2], land[i-1][j+3])
#             elif j == 1:
#                 land[i][j] += max(land[i-1][j-1], land[i-1][j+1], land[i-1][j+2])
#             elif j == 2:
#                 land[i][j] += max(land[i-1][j-2], land[i-1][j-1], land[i-1][j+1])
#             else:
#                 land[i][j] += max(land[i-1][j-3], land[i-1][j-2], land[i-1][j-1])

#     return max(land[-1])