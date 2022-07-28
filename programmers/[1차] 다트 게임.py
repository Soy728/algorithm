# 2018 KAKAO BLIND RECRUITMENT [1차] 다트 게임
#2022.07.28 -> soy birthday


def solution(dartResult):
    answer = []
    idx = -1 #answer 리스트의 인덱스
    number =""
    
    for i in dartResult:
        if i.isdigit(): # 숫자면 number에 저장
            number = number + i
        elif i.isalpha(): #문자면 숫자를 answer 리스트에 넣기
            if i == "S":
                answer.append(int(number))
            elif i == "D":
                answer.append(int(number)**2)
            elif i == "T":
                answer.append(int(number)**3)
            idx += 1 # answer에 숫자 하나 넣었으니까 idx 증가
            number = ""
                
        elif i == "*":
            if len(answer) == 1:
                answer[idx] = answer[idx] *2
            else:
                answer[idx-1],answer[idx] = answer[idx-1] *2,answer[idx] *2
        
        elif i == "#":
            answer[idx] = -answer[idx]
            
    #합산        
    ans = 0    
    for i in answer:
        ans += i
            
    return ans