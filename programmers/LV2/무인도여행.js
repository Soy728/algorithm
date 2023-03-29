function solution(maps) {
  // 1. maps로 들어온 string 배열을 2차원 배열로 변환
  // 2. visited 배열을 maps 배열과 같은 크기로 만든뒤 모두 false 값으로 초기화
  // 3. visited가 false이고 maps[i][j]가 X가 아니라면 BFS 탐색 시작
  // 4. 큐에 값을 상하좌우 isited가 false이고 maps[i][j]가 X가 아닌 좌표값을 넣는다. 내가 지금 위치한 좌표의 숫자를 sum에 더하고 visited를 true로 바꾼다.
  // 5. 큐가 빌 때까지 반복한다.
  // 6. 큐에 값이 없으면 sum을 배열에 push한뒤 0으로 초기화한다.
  // 7. 탐색이 끝났다면 배열을 오름차순 정렬한다.

  let answer = [];
  let mapArray = maps.map((d) => d.split(""));
  let visited =  Array.from(Array(maps.length),() => new Array(maps[0].length).fill(false));

  let queue = [];


  for (j = 0; j < maps.length ; j++) { 
    for (i = 0; i < maps[0].length; i++) { 

      if (mapArray[j][i] != "X" && visited[j][i] == 0) { 
     
        queue.push([j, i]);
        visited[j][i] = 1;
       
        let sum = Number(mapArray[j][i]);
        const dy = [1, 0, -1, 0];
        const dx = [0, 1, 0, -1];
      
        while (queue.length != 0) { 
          let [y, x] = queue.shift();
          for (z = 0; z < 4; z++) { 
            let searchX = x + dx[z];
            let searchY = y + dy[z];
          
            if (0 <= searchX  && searchX < maps[0].length && 0 <= searchY && searchY< maps.length && visited[searchY][searchX] == 0 && mapArray[searchY][searchX] != "X") { 
              visited[searchY][searchX] = 1;
              queue.push([searchY, searchX]);
              sum += Number(mapArray[searchY][searchX]);
            }
            
          }
        }
        answer.push(sum)
      }

    }
  }
            
 
  answer.sort((a, b) => (a - b))
  answer.length == 0 && answer.push(-1)
  return answer;
}

solution(["X591X","X1X5X","X231X", "1XXX1"])