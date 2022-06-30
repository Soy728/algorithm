def solution(s):
    answer = []
    
    if len(s)==1:
        return 1
    
    for step in range(1, (len(s)//2)+1):
        compressed = ""
        prev = s[:step]
        count = 1
        
        for j in range(step, len(s), step):
            if s[j:j+step] == prev:
                count += 1
                
            else:
                if count >1:
                    compressed += str(count)+prev 
                else: compressed += prev 
                prev = s[j:j+step]
                count = 1
                
        if count >1:
                    compressed += str(count)+prev 
        else: compressed += prev

        answer.append(compressed)
        
    return len(min(answer, key=len))
