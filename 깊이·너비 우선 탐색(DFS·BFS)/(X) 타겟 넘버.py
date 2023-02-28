def solution(numbers, target):
    super_node = [0]
    for number in numbers:
        sub_node = []
        for sup in super_node:
            sub_node.append(sup + number)
            sub_node.append(sup - number)
        super_node = sub_node    
    return super_node.count(target)
