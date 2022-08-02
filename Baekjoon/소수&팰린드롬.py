#BOJ Silver 1 1747번
#에라토스테네스의 체 - 소수 구하기 
#2022.08.02

import math

m = 2000000
num = int(input())
prime = [False]*2+[True]*(m)

for i in range(2,int(math.sqrt(m)+1)):
    if prime[i] == True:
        for j in range(i+i,m,i):
            prime[j] = False


for i in range(num,m):
    if str(i) == str(i)[::-1]:
        if prime[i] == True:
            result = i
            print(result)
            break
