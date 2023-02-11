def solution(answers):
    answer = []
    scores = [0,0,0]
    
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == a1[i % len(a1)]:
            scores[0] += 1
            
        if answers[i] == a2[i % len(a2)]:
            scores[1] += 1
            
        if answers[i] == a3[i % len(a3)]:
            scores[2] += 1    
    
    max_score = max(scores)
        
    for i in range(len(scores)):
         if scores[i] == max_score:
            answer.append(i+1)
    answer.sort()        
   

    return answer