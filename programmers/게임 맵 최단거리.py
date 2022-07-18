# 프로그래머스 bfs/dfs 게임 맵 최단거리 
# 20220718

from collections import deque


def solution(maps):
    answer = -1

    visited = [[False for i in range(len(maps[0]))] for j in range(len(maps))]
    queue = deque()
    queue.append((0,0))
  
   
    visited[0][0] = 1 

    while queue:
        
        x,y = queue.popleft()
        
        for i in range(4):

            dx=[1,0,-1,0]
            dy=[0,1,0,-1]

            searchX = x+dx[i]
            searchY = y+dy[i]

            if 0<=searchX<len(maps) and 0<=searchY<len(maps[0]) and visited[searchX][searchY] == False and maps[searchX][searchY]==1:
                 queue.append((searchX,searchY))
                 visited[searchX][searchY] = visited[x][y]+1
            
         
    if visited[-1][-1] != False: answer =  visited[-1][-1]
    
    return answer

