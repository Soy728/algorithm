// 문제 해결중


// 레버가 있는 좌표를 구한 뒤, 레버에 도달할 수 있는지를 먼저 판단한다.
// 레버에 도달 할 수 없다면 -1을 반환.
// 레버에 도달 할 수 있다면 탈출구에 도달 할 수 있는지를 판단한다.

function solution(maps) {
  
  let lever;
  let start;
  let end;
  let arr = maps.map((d, i) => {
    d.indexOf("L") !== -1 && (lever = [i, d.indexOf("L")])
    d.indexOf("S") !== -1 && (start = [i, d.indexOf("S")])
    d.indexOf("E") !== -1 && (end = [i,d.indexOf("E")])
    return d.split("")
  });

  function BFS(start, end) {
    let answer = 0;
    let visited = Array.from(Array(maps.length),() => new Array(maps[0].length).fill(false));
    let queue = [];
    queue.push(start);
    visited[start[0]][start[1]] = 1;

        while (queue.length > 0) { 
          let [y, x] = queue.shift();
          const dy = [1, 0, -1, 0];
          const dx = [0, 1, 0, -1];
          for (z = 0; z < 4; z++) { 
          let searchX = x + dx[z];
          let searchY = y + dy[z];
      
            if (0 <= searchX && searchX < maps[0].length && 0 <= searchY && searchY < maps.length && arr[searchY][searchX] != 'X' && visited[searchY][searchX] == 0) {
            visited[searchY][searchX] = 1;
            queue.push([searchY, searchX]);

              if (searchY == end[0] && searchX == end[1]) {
                return answer + 1;
                
       }
        }
       
          }
          answer += 1;
        }
     return -1
}

  
  let statToLever = BFS(start, lever)
  console.log(statToLever)
  if (statToLever == -1) {
    return -1
  }
  else { 
    let leverToEnd = BFS(lever, end)
    console.log(leverToEnd)
    if (leverToEnd == -1) {
      return -1
    }
    else { return statToLever+ leverToEnd} 
  }

}


let ans = solution(["OOOOOL", "OXOXOO", "OOSXOX", "OXXXOX", "EOOOOX"])
console.log(ans)

// [ "XXXXXL",
//   "XXXXOO",
//   "OOSXOX",
//   "OXXXOX",
//   "EOOOOX"]
//   (4,1)

// [ "OOOOOL",
//   "OXOXOO",
//   "OOSXOX",
//   "OXXXOX",
//   "EOOOOX"]