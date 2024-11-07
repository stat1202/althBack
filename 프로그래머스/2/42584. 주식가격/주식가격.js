function solution(prices) {
    const L = prices.length
    const answer = Array(L).fill(0)
    
    for(let i = 0; i < L; i++){
        let cnt = 0
        for(let j = i+1; j < L; j++){
            if(prices[i] <= prices[j]){
                cnt += 1
            }
            else{
                if( i !== L-1){
                    cnt += 1
                }
                break
            }
        }
        answer[i] = cnt
    }
    
    return answer;
}