 const getPermutations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el]);

    arr.forEach((fixed, index, origin) => {
      const rest = [...origin.slice(0, index), ...origin.slice(index+1)] 
      const permutations = getPermutations(rest, selectNumber - 1); 
      const attached = permutations.map((el) => [fixed, ...el]); 
      results.push(...attached); 
    });

    return results; 
}


function divideString(arg) { 
    let arr = [];
    let str = ''
    for (i = 0; i < arg.length; i++) { 
        if (!isNaN(arg[i])) {
            str += arg[i]
        }
        else {
            arr.push(str);
            str = ''
            arr.push(arg[i])
        }
    }
    arr.push(str);
    return arr;

}
function solution(expression) {
    let answer = [];
    let operArr=[];

    for(i = 0 ; i<expression.length ; i++){
       isNaN(expression[i]) && !operArr.includes(expression[i])&& operArr.push(expression[i]);
    }

    let arr = divideString(expression);
    let permuArr = getPermutations(operArr, operArr.length);
    let stack = [];
    
    for (i = 0; i < permuArr.length; i++) { 
        stack.push(Number(expression[0]));
        let permuArrIndex = 0;
        while (stack.length > 1) {
            let sign = permuArr[i][permuArrIndex];
              for(z = 1 ; z<expression.length ; z++){
                  if (!isNaN(expression[z])) {
                      stack.push(Number(expression[z]))
                      //number 라면 stack에 넣는다.
                      
                  } else { 
                      
                      //number가 아니라면 stack에서 pop하고 다음 expression[z+1]과 연산한 후에 스택에 넣는다.
                  }
              }
            permuArrIndex += 1;
           
    }

    

    }
   
  
    



  
    return answer;
}



solution("50*6-3*2")
//node programmers/LV2/수식최대화.js