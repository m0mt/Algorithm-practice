# 인덱스 이용하는 법
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        tree_idx = [skill_tree.index(i) for i in skill if i in skill_tree]
        # for i in range(len(skill)):
        #     tree_idx.append(skill_tree.find(skill[i]))
            
        tree_idx_ = sorted(tree_idx)
        print(tree_idx)
        if tree_idx == tree_idx_ :
            answer += 1
            
        

            

                
        
    return answer   
# 문자열 자체를 이용하는 법
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))