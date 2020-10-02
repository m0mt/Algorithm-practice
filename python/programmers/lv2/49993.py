## 인덱스 이용하는 법

# def solution(skill, skill_trees):
#     answer = 0
#     for skill_tree in skill_trees:
#         tree_idx = [skill_tree.index(i) for i in skill if i in skill_tree]
            
#         tree_idx_ = sorted(tree_idx)
#         print(tree_idx)
#         # 스킬트리가 1개 일때, C는 무조건 있어야 하고
#         # 2개일 때 , CB
#         # 3개일 때 , CBD 하기 때문에 and 조건 추가
#         if tree_idx == tree_idx_ and all(i in skill_tree for i in skill[:len(tree_idx)]):
#             answer += 1
        
#     return answer   

## 문자열 자체를 이용하는 법

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        temp = []
        for sk in tree:
            if sk in skill:
                temp.append(sk)

        flag = True
        for i in range(len(temp)):
            if temp[i] != skill[i]:
                flag = False
                break
        if flag:
            answer += 1
                
    print(skill_trees)
    return answer
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))