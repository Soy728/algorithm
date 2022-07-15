size = int(input())
ocean = []
ans = 0 

for _ in range(size):
    temp_ocean = list(map(int,input().split()))
    ocean.append(temp_ocean)

for i in range(size): #아기상어 처음 위치 찾기
    for j in range(size):
        if ocean[i][j] == 9:
            x1,y1 =i,j


level = 2 # 레벨. eatenNum이 level과 같아지면 +1 씩증가 
EatenNum = 0 # 먹으면 +1 씩증가 

Queue = []
Queue.append([x1,y1])

visited = [[0 for _ in range(size)] for _ in range(size)] 
visited[x1][y1] = 1
ocean[x1][y1] = 0 #아기상어 있던자리 0으로 만들기
temp = []

while True:
    while Queue != []:
        x,y = Queue.pop(0)
    
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
    
        for i in range(4): 
            searchX = x+ dx[i]
            searchY = y+ dy[i]
        

            if 0<=searchX<size and 0<=searchY<size: #범위 벗어나지 않고
                if visited[searchX][searchY] == 0: #아직 방문하지 않았다면
                    if ocean[searchX][searchY] <= level: #지나갈수 있으면 큐에 넣기
                        Queue.append([searchX,searchY])
                  
                        visited[searchX][searchY] = visited[x][y]+1 #거리 계산
     
                    if 0< ocean[searchX][searchY] < level: #먹을 수 있으면 temp에 저장
                        temp.append([visited[searchX][searchY],searchX,searchY])
                        

    if temp != []: 
        
        temp.sort(key=lambda x :(x[0],x[1],x[2])) #가장 가까운 거리 계산
        ans += visited[temp[0][1]][temp[0][2]]-1  #가장 가까운 거리, 혹은 가까운 거리가 많다면 맨 위쪽, 맨 왼쪽 지점의 물고기 먹기
        EatenNum += 1

        visited = [[0 for _ in range(size)] for _ in range(size)] 
        ocean[temp[0][1]][temp[0][2]] = 0

        Queue = []
        Queue.append([temp[0][1],temp[0][2]])
        visited[temp[0][1]][temp[0][2]] = 1
    
    else: #temp가 비어있으면 먹을게 없다는 뜻. 반복문 탈출.
        break

    temp = []
        
    if EatenNum == level: #level만큼 물고기를 먹었다면 level +1
        level += 1
        EatenNum = 0

print(ans)

               

            
