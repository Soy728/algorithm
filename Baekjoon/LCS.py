def longestCommonSubsequence(text1: str, text2: str):
        lentext1 = len(text1)
        lentext2 = len(text2)
        table = [[0 for i in range(lentext1+1)] for i in range(lentext2+1)]
    
        for i in range(lentext2+1):
            for j in range(lentext1+1):
                if i==0 or j==0:
                    table[i][j] = 0
                elif text2[i-1] == text1[j-1]:
                    table[i][j] = table[i-1][j-1]+1
                else:
                    table[i][j] = max(table[i][j-1],table[i-1][j])
                    
        return table[lentext2][lentext1]
    
text1 = input()
text2 = input()
print(longestCommonSubsequence(text1,text2))