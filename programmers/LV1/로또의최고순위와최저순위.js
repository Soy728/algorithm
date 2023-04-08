// 2021 Dev-Matching

function solution(lottos, win_nums) {
    let answer = [];
    let least = 0;
    let most = 0;
    const lottoRank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    
    for(i=0;i<lottos.length;i++) {
 
        if(win_nums.includes(lottos[i])>0){
           win_nums = win_nums.filter((d)=> d != lottos[i])
            console.log(lottos[i], win_nums)
           least +=1
           most +=1
           }
        else if(lottos[i] == 0){
            most +=1
        }
    }
    answer.push(lottoRank[most])
    answer.push(lottoRank[least])
    


    return answer;
}
solution([44, 1, 0, 0, 31, 25],	[31, 10, 45, 1, 6, 19] )

//node programmers/LV1/로또의최고순위와최저순위.js