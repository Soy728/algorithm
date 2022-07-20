#프로그래머스 프린터 LV2
#2022.07.21

def solution(priorities, location):
    answer = 0
    
    while True:
        count = True #append 했는지 안했는지 표시하는 변수
        wait = priorities.pop(0)
        for i in priorities:
            if wait<i: # pop한거보다 큰 값이 있으면 append, count는 false로
                priorities.append(wait) 
                count = False
                break
        
        if count == True: #append하지 않았다 = 프린트했다.
            answer += 1 # 프린트 했으므로 answer ++
            if location == 0: #뽑은게 location이라면 return
                return answer
                
        location = location -1 #반복문 1회 진행하면 location의 index -1 해줘야함
        if location < 0: #location이 맨 뒤로가면 인덱스 조정
            location = len(priorities)-1