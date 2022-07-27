#백준 최소비용 구하기 Gold 5
#2022.07.28
#주의: 버스 양방향이 아님. 단방향임...
import heapq
import sys

def dijkstra(adj,distance,start):
    heap = []
    heapq.heappush(heap,[0,start])
    while heap != []:
        cost, node = heapq.heappop(heap)

        if cost > distance[node]: #distance에 기록된 cost보다 현재 cost가 더 크면 볼 필요도 없음
            continue

        else:
            for c,n in adj[node]:
                if distance[n]>cost+c:
                    distance[n] = cost+c
                    heapq.heappush(heap,[cost+c,n])
        
        
numOfCity = int(sys.stdin.readline())
numOfBus = int(sys.stdin.readline())

INF = float('inf')
distance = [INF]*(numOfCity+1)
adj = [[] for _ in range(numOfCity+1)]


for i in range(numOfBus):
    city1, city2, cost = map(int, sys.stdin.readline().split())
    adj[city1].append([cost,city2])


start, dest = map(int, sys.stdin.readline().split())
distance[start]= 0 #자기자신과의 거리는 0

dijkstra(adj,distance,start)

print(distance[dest])






