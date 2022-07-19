#BOJ 13414:수강신청, Sliver 3
#20220719
#리스트를 사용하면 remove하는데 시간초과남 -> 딕셔너리 사용하기

student,inputnum = map(int,input().split(" "))
waiting = {}

for i in range(inputnum):
    studentNumber = input()
    waiting[studentNumber] = i
    
waiting = dict(sorted(waiting.items(), key=lambda x:x[1]))

    
count = 0
for key in waiting.keys():
    print(key)
    count +=1
    if count == student: break