#BOJ 1920 Sliver 4
#2022.07.26
#Binary search

n = int(input())
numbersN=list(map(int,input().split()))

m = int(input())
numbersM=list(map(int,input().split()))

numbersN.sort()

for j in numbersM: #j가 target 숫자
    start = 0
    end = n-1
    noelement = True
    
    while start <= end:
        mid = (start+end)//2
        if j == numbersN[mid]:
            print(1)
            noelement = False
            break
        elif j>numbersN[mid]:
            start = mid+1
        else:
            end = mid -1
    
    if noelement:
        print(0)