// dic에 key(문자) : val(인덱스)
// 문자열 s 돌면서 없으면 dic에 넣고 answer에 -1 넣기
// 있으면 자신의 인덱스와 비교 후에 answer 에 자기자신 - 이전값 넣기, 인덱스 자기 자신으로 바꾸기


function solution(s) {
    let dic = {}
    let answer = [];
    
    for(i = 0; i < s.length ; i++){
        if (s[i] in dic){
            let temp  =dic[s[i]] 
            dic[s[i]] = i
            answer.push(i-temp)
        }else{
            dic[s[i]] = i
            answer.push(-1)
        }
        
    }
    return answer;
}