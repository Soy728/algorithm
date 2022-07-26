#프로그래머스 Summer/Winter Coding(~2018) 배달 level 2
#2022.07.27
#다익스트라 알고리즘 

import heapq

def dijkstra(distance,adj):
    heap = []
    heapq.heappush(heap,[0,1]) #node 1 부터 시작, cost는 0
    while heap != []:
        cost, node = heapq.heappop(heap)
        
        for c,n in adj[node]: #adj의 거리보다 현재노드를 거치는 cost가 더 적으면 갱신
            if distance[n]>cost+c:
                distance[n] = cost+c
                heapq.heappush(heap,[cost+c,n])
                

def solution(N, road, K):
    answer = 0
    INF = float('inf')
    distance = [INF]*(N+1)
    distance[1] = 0 #node 1인 자기자신의 거리는 0
    adj = [[] for _ in range(N+1)]
    
    for i in road:
        adj[i[0]].append([i[2],i[1]])
        adj[i[1]].append([i[2],i[0]])
        
    dijkstra(distance,adj)
    
    for i in distance:
        if i <= K:
            answer += 1
    
    return answer