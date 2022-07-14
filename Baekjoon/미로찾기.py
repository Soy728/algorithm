x,y = map(int, input().split())
maze = []
visited = [[0 for _ in range(y)] for _ in range(x)]

for i in range(x):
    temp_maze = list(input())
    maze.append(temp_maze)

Queue = []
Queue.append([0,0])
visited[0][0]= 1
while Queue != []:
    x_,y_ = Queue.pop(0)
 
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    for i in range(4):
        searchX = x_+ dx[i]
        searchY = y_+ dy[i]

        if 0<=searchX<x and 0<=searchY<y and  visited[searchX][searchY] == 0:
            if maze[searchX][searchY] =='1':
                Queue.append((searchX,searchY))
                visited[searchX][searchY]= visited[x_][y_]+1
          
         
print(visited[x-1][y-1])





    

