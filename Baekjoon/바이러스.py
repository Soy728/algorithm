numOfComputer = int(input())
pairs = int(input())
linked = []
visited = []
linkans = 0
computer = [[0 for col in range(numOfComputer)] for row in range(numOfComputer)]

for _ in range(pairs):
    x, y = map(int,input().split())
    computer[x-1][y-1] = 1
    #단방향 그래프임


linked.append(0)
visited.append(0)

while linked != []:
    
    search = linked.pop(0)
    for i in range(len(computer)):
        if computer[search][i] == 1 or computer[i][search] == 1:
            if i not in visited:
                linked.append(i)
                visited.append(i)
                linkans += 1
                        
      
print(linkans)


