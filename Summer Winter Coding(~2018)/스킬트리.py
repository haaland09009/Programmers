def solution(skill, skill_trees):
    count = 0 # 불가능한 스킬트리의 수
    skill_list = []

    for tree in skill_trees:
        skill_list = list(skill)
        for t in tree:
            if t in skill_list and t == skill_list[0]:
                skill_list.pop(0)
            elif t in skill_list and t != skill_list[0]:
                count += 1 # 불가능한 스킬트리 추가
                break

    return len(skill_trees) - count # 전체 스킬트리 중에서 불가능한 스킬트리를 제외한 수