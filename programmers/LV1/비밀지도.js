// arr1,2 각 수를 이진수로 변환 후에 배열에 저장, 2차원 배열
// 이진수 변환:  num.toString(2);
// 공백 문자열 0으로 채우기: string.padStart(n,0);

function solution(n, arr1, arr2) {
    let answer = []
  for (i = 0; i < n;  i++){
    let binaryResult = "";
    let binaryArr1 = arr1[i].toString(2).padStart(n, 0); 
    let binaryArr2 = arr2[i].toString(2).padStart(n,0);

    for (j = 0; j < n; j++){
            binaryResult += (Number(binaryArr1[j]) || Number(binaryArr2[j])) ? '#': ' ';
        }
    answer.push(binaryResult);
    }
    return answer;
}
