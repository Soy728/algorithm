def solution(numbers, target):
    answer = 0
    n = len(numbers)

    
    def dfs_search(idx,result):
        if idx == n: # leaf노드 이후 idx도달시 target과 비교
            if target == result:
                nonlocal answer
                answer += 1
            return
        else:
            dfs_search(idx+1,result+numbers[idx])
            dfs_search(idx+1,result-numbers[idx])
            
    dfs_search(0,0)
    
    return answer
