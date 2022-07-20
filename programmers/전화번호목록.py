#프로그래머스 전화번호 목록 lv2
#20220721

def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        short_number = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:short_number]:
            answer = False
            return answer
        
    return answer