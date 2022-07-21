#프로그래머스 다리를 지나는 트럭 LV2
#2022.07.22
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length) #다리 만들기
    nowweight = 0 #현재 다리위에 있는 트럭 무게의 합
    truck_weights = deque(truck_weights)

    #다리에 처음으로 들어오는 트럭 처리 
    entrance = truck_weights.popleft()
    bridge.append(entrance)
    nowweight += entrance
    bridge.popleft()
    answer += 1

    while len(truck_weights) != 0:

        #다리에 새 트럭이 올라갈 수 있는 경우
        if nowweight+truck_weights[0]-bridge[0] <= weight:
            if truck_weights != []:
                entrance = truck_weights.popleft()
                bridge.append(entrance)
                out = bridge.popleft()

        #다리에 새 트럭이 올라갈 수 없는 경우        
        else:
            entrance = 0
            bridge.append(0)
            out = bridge.popleft()

        nowweight += entrance
        nowweight -= out
        answer += 1
        
    #대기트럭은 없지만 다리에 남아있는 트럭이 다리를 다 건널 때 까지 시간 세기
    for i in range(len(bridge)-1,-1,-1):
        if bridge[i] != 0: #가장 늦게 들어온 트럭이 다리를 다 건너는 시간을 세야하므로 맨뒤에 있는 트럭을 찾음.
            answer += i+1
            break
            
    
    return answer