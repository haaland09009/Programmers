def solution(n, lost, reserve):
    reserve_person = set(reserve) - set(lost)
    lost_person = set(lost) - set(reserve)
    
    for r in reserve_person:
        if r-1 in lost_person:
            lost_person.remove(r-1)
        elif r+1 in lost_person:
            lost_person.remove(r+1)

    return n - len(lost_person)