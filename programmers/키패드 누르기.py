def solution(numbers, hand):
    answer = ''
    keypad = {"*":[0,0], "0":[0,1], "#":[0,2], "7":[1,0], "8":[1,1], "9":[1,2], "4":[2,0], "5":[2,1], "6":[2,2], "1":[3,0], "2":[3,1], "3":[3,2]}
    
    leftPos = keypad["*"]
    rightPos = keypad["#"]
    for i in numbers:
        if i in [1,4,7]:
            answer += "L"
            leftPos = keypad[str(i)]
            
        elif i in [3,6,9]:
            answer += "R"
            rightPos = keypad[str(i)]
           
        else:
            midPos = keypad[str(i)]
            rightlen = abs(midPos[0]-rightPos[0])+abs(midPos[1]-rightPos[1])
            leftlen = abs(midPos[0]-leftPos[0])+abs(midPos[1]-leftPos[1])
            if rightlen>leftlen:
                answer += "L"
                leftPos =midPos
                
            elif rightlen<leftlen: 
                answer +="R"
                rightPos = midPos
                
            else:
                if hand == "right":
                    answer += "R"
                    rightPos = midPos
                   
                else:
                    answer += "L"
                    leftPos = midPos          

    return answer
