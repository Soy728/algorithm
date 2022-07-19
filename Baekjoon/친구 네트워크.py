#BOJ 4195:친구 네트워크, gold 2
#20220719
#union-find문제, 딕셔너리 사용

import sys

loop = int(sys.stdin.readline())

def find_parent(x):
    if network[x] != x: #같지 않으면 루트노드 찾을때 까지 재귀적으로 호출
        network[x] = find_parent(network[x])

    #같으면 나 자신이 부모임
    return network[x]

def union(friend1,friend2):
    friend1 = find_parent(friend1)
    friend2 = find_parent(friend2)

    if friend1 != friend2:
        network[friend2] = friend1
        child[friend1] += child[friend2]

for i in range(loop):
    loop2 = int(sys.stdin.readline())
    network ={}
    child ={}
    
    for j in range(loop2):
        friend1, friend2 = sys.stdin.readline().split()

        #네트워크에 없는 참여자라면 네트워크에 넣기, 부모는 자기자신으로 초기화
        if friend1 not in network:
            network[friend1] = friend1
            child[friend1] = 1
        if friend2 not in network:
            network[friend2] = friend2
            child[friend2] = 1
        
        union(friend1,friend2)
        print(child[find_parent(friend1)])

        

        
        



