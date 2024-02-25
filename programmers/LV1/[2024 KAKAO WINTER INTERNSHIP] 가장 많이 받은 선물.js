function solution(friends, gifts) {
  let entireCount = {};
  let giveGiftsCount = {};
  let receiveGiftsCount = {};

  let nextMonth = {};
  let giftScore = {};

  friends.map((v) => {
    giveGiftsCount[v] = 0;
    receiveGiftsCount[v] = 0;
    giftScore[v] = 0;
    nextMonth[v] = 0;

    friends.map((a) => {
      if (v !== a) {
        const string = [v, a].join(' ');
        entireCount[string] = 0;
      }
    });
  });

  gifts.map((v) => {
    const giver = v.split(' ')[0];
    const getter = v.split(' ')[1];

    if (entireCount[v]) {
      entireCount[v] = entireCount[v] + 1;
    } else {
      entireCount[v] = 1;
    }

    giveGiftsCount[giver] = giveGiftsCount[giver] + 1;
    receiveGiftsCount[getter] = receiveGiftsCount[getter] + 1;
  });

  friends.map((v) => {
    giftScore[v] = giveGiftsCount[v] - receiveGiftsCount[v];
  });

  Object.entries(entireCount).map((v, i) => {
    const forwardString = v[0];
    const forward = forwardString.split(' ');
    const backwardString = [forward[1], forward[0]].join(' ');

    if (
      v[1] >
      Object.entries(entireCount)
        .slice(i)
        .find((v) => v[0] == backwardString)?.[1]
    ) {
      nextMonth[forward[0]] = nextMonth[forward[0]] + 1;
    } else if (
      v[1] <
      Object.entries(entireCount)
        .slice(i)
        .find((v) => v[0] == backwardString)?.[1]
    ) {
      nextMonth[forward[1]] = nextMonth[forward[1]] + 1;
    } else if (
      v[1] ==
      Object.entries(entireCount)
        .slice(i)
        .find((v) => v[0] == backwardString)?.[1]
    ) {
      if (giftScore[forward[1]] > giftScore[forward[0]]) {
        nextMonth[forward[1]] = nextMonth[forward[1]] + 1;
      } else if (giftScore[forward[1]] < giftScore[forward[0]]) {
        nextMonth[forward[0]] = nextMonth[forward[0]] + 1;
      }
    }
  });

  return Math.max(...Object.values(nextMonth));
}
