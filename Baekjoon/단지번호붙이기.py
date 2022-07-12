import sys
from collections import deque
num = int(input())
array = [] #2차원 배열 저장
for i in range(num):
    string = list(input())
    array.append(string) 

countofArea = 0

visited = [[False for col in range(num)] for row in range(num)]
Queue = deque()
answer =[]


for i in range(num):
    for j in range(num):
        
        if array[i][j] != '1' or visited[i][j] == True:
            continue;
        
        Queue.append([i,j])
        visited[i][j] = True
        countofArea +=1 
        sizeofArea = 0
        
        while Queue:
            x, y = Queue.popleft()
            
            
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            
            for a in range(4):
                searchX = x + dx[a]
                searchY = y + dy[a]
                
               
                if (0<=searchX<num) and (0<=searchY<num) and array[searchX][searchY] == '1' and visited[searchX][searchY] == False:
                        visited[searchX][searchY] = True
                        Queue.append([searchX,searchY])
            sizeofArea += 1
               
        answer.append(sizeofArea)


answer.sort()

print(countofArea)
for i in answer:
    print(i)













