def solution(cards1, cards2, goal):
    answer = "Yes"
    for i in range(len(goal)):
        if goal[i] in cards1 and goal[i] == cards1[0]:
            cards1.pop(0)
        elif goal[i] in cards1 and goal[i] != cards1[0]:
            answer = "No"
            break
        if goal[i] in cards2 and goal[i] == cards2[0]:
            cards2.pop(0)
        elif goal[i] in cards2 and goal[i] != cards2[0]:
            answer = "No"
            break

    return answer