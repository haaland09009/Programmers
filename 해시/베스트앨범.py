# https://school.programmers.co.kr/learn/courses/30/lessons/42579/

# 직접 해결한 풀이

def solution(genres, plays):
    answer = []
    
    sum_dic = {}
    dic = {}
    
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = [(i, plays[i])]
            sum_dic[genres[i]] = [plays[i]]
        else:
            dic[genres[i]].append((i, plays[i]))
            sum_dic[genres[i]].append(plays[i])
   
    for k,v in sorted(sum_dic.items(), key=lambda x:sum(x[1]), reverse=True):
        for key,value in sorted(dic[k], key=lambda x:(x[1], -x[0]), reverse=True)[:2]:
             answer.append(key)
        

    return answer



#  개선 풀이
# def solution(genres, plays):
#     answer = []
    
#     dic1 = {}
#     dic2 = {}
    
#     for i, (g,p) in enumerate(zip(genres, plays)):
#         if g not in dic1:
#             dic1[g] = [(i,p)]
#         else:
#             dic1[g].append((i,p))
        
#         if g not in dic2:
#             dic2[g] = p
#         else:
#             dic2[g] += p
            
#     for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
#         for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
#             answer.append(i)
#     return answer