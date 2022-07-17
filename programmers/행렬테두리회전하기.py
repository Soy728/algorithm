def solution(rows, columns, queries):
    answer = []
    index = []
    #행렬 생성
    array = [[0 for j in range(columns)] for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            array[i][j] = ((i)*columns + (j+1))
            
            
    for i in range(len(queries)):
        lefty, leftx = queries[i][0]-1, queries[i][1]-1 
        righty, rightx = queries[i][2]-1, queries[i][3]-1 
        
        startpoint = array[lefty][leftx]
        minimum = startpoint
        
        #왼쪽 위로 올리기
        for j in range(lefty,righty):
            temp = array[j+1][leftx]
            print(j)
            array[j][leftx] = temp
            
            minimum = min(minimum, temp)
        #아래쪽 왼쪽으로 
        for j in range(leftx,rightx): 
            temp = array[righty][j+1]
            array[righty][j] = temp
            minimum = min(minimum, temp)

        #오른쪽 아래로 
        for j in range(righty,lefty,-1):
            temp = array[j-1][rightx]
            array[j][rightx] = temp
            minimum = min(minimum, temp) 
       
        #위쪽 오른쪽으로
        for j in range(rightx,leftx,-1):
            temp = array[lefty][j-1]
            array[lefty][j] = temp
            minimum = min(minimum, temp)
        
            
        array[lefty][leftx+1] = startpoint
        answer.append(minimum)
            

        
    return answer

print(solution(100,97,[[1,1,100,97]]))