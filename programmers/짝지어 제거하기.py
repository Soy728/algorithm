def solution(s):
    
    if len(s)==1:
        return 0
    
    stackstr = [s[0]]
    
    #stack 이용하여 풀기
    for i in s[1:]:
        if stackstr != []:            #stack이 비어있지않고
            if stackstr[-1] == i:     #top과 같으면 pop해서 지우기
                stackstr.pop()
            else:                     #top과 다르면 append
                stackstr.append(i)
        else:                         #스택이 비어있으면 append
            stackstr.append(i)
            
    if stackstr == []:
        return 1
    else:
        return 0