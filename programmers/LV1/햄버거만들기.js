
//시간 초과 났던 코드
// 햄버거를 만들고 나서 다시 처음부터 ingredient를 돌기 때문에 시간초과가 발생한다.
// 따라서 햄버거를 만들고 난 뒤, 현재 위치에서 검사를 진행하는 방식으로 코드를 짜야하며 이는 stack으로 구현 할 수 있다.
 
function solution(ingredient) {
  let answer = 0;
  let enable = true;
  let i = 0;
  while (enable) { 
    if (ingredient[i] == '1' && ingredient[i + 1] == '2' && ingredient[i + 2] == '3' && ingredient[i + 3] == '1') {
      ingredient.splice(i, 4);
      answer += 1;
      i = 0;
    }
    else { i += 1}
   
    if ( i > ingredient.length-3) { 
      enable = false;
    }
  }
    return answer;
}

//성공한 코드
function solution(ingredient) {
  let answer = 0;
  const stack = [];

  for (let i = 0; i < ingredient.length; i++) {
    stack.push(ingredient[i]);

    if (stack.slice(-4).join('') == '1231') {
      stack.splice(-4);
      answer++;
    }
  }
  return answer;
}