// {문자열 : 횟수} 형태의 딕셔너리 생성
// 딕셔너리의 value들로 set 객체 생성하여 중복 없애기
// set과 딕셔너리의 length가 다르다면 같은 횟수가 등장한 것으로 판단하고 문자열을 split, answer += 1
// split되면 위의 과정 반복 
function solution(string) {
  let answer = 0;
  let dic = {};
  let s = 0;
  
  while (true) {
    if (Object.keys(dic).includes(string[s])) {
      dic[string[s]] += 1;
    } else {
      dic[string[s]] = 1;
    }
    let set = [...new Set(Object.values(dic))];
    console.log(dic,set)
    if (set.length != Object.keys(dic).length) {
      console.log(dic)
      string = string.substr(s + 1)
      dic = {}
      set = []
      answer += 1;
      s = 0;
      
    } else { 
      s += 1;
    }
    
    if (s >= string.length)
    { if(string.length != 0){
        answer += 1
    }
      return answer;
    }
    
  }

}


console.log(solution("abaabc"))

//node programmers/LV1/문자열나누기.js