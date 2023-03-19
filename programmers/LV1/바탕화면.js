function solution(wallpaper) {
  let result = [];
  let y = [];
  let x = [];
  let answer = wallpaper.map((d)=> [...d]);  
  answer.map((d, i) => { d.map((v, i2) => { if (v == "#") { x.push(i2); y.push(i) } }) });

  y.sort((a, b) => a - b);
  x.sort((a, b) => a - b);
    
  result.push(y[0], x[0], y[y.length - 1] + 1, x[x.length - 1] + 1);
  return result;
    
}

let a = new Date('2022-02-01').getTime()
console.log(a)