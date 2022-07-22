#프로그래머스 구명보트 lv2
#2022.07.23
#그리디 초이스는 가장 가벼운 사람과 가장 무거운 사람을 실어서 보내는 것. 조건에 만족하지 않는 경우에는 가장 무거운 사람을 먼저 실어보냄. 그리고 그리디 초이스 계속 반복!

from collections import deque
def solution(people, limit):

    answer = 0
    people.sort()
    people = deque(people)
    
    while len(people) > 0:
        if len(people)>=2 and people[0]+people[-1]<= limit: #두 명을 한 보트에 싣는 경우
                people.popleft()
                people.pop()
        else: #한 명만 보트에 싣는 경우
            people.pop()
        
        answer += 1

    return answer
