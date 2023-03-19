function solution(today, terms, privacies) {
    let answer= []
    const termsDict = {}
    terms.map((d) => { termsDict[d[0]] = Number(d.slice(2, d.length)) })
    let now = today.split(".").map(Number);

    privacies.map((d, i) => {
        const [type, term] = d.split(" ");
        let date = type.split(".").map(Number)
        date[1] = Number(date[1]) + termsDict[term]
        const year = Math.floor(date[1] / 12)
        date[1] > 12 && (date[0] = Number(date[0]) + year) && (date[1] = date[1] - (12 * year))

        if ((now[0] - date[0]) * 12 * 28 + (now[1] - date[1]) * 28 + (now[2] - date[2]) >= 0) answer.push(i + 1);

    })

    return answer;
}
