function parseInt(string) {
  const small = {
    zero: 0,
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9,
    ten: 10,
    eleven: 11,
    twelve: 12,
    thirteen: 13,
    fourteen: 14,
    fifteen: 15,
    sixteen: 16,
    seventeen: 17,
    eighteen: 18,
    nineteen: 19,
    twenty: 20,
    thirty: 30,
    forty: 40,
    fifty: 50,
    sixty: 60,
    seventy: 70,
    eighty: 80,
    ninety: 90,
  };

  const multi = {
    hundred: 100,
    thousand: 1000,
    million: 1000000,
  };

  const result = string
    .toLowerCase()
    .split(/\s+|-/)
    .reduce(
      (acc, cur) => {
        if (cur in small) acc.running += small[cur];
        if (cur in multi) {
          acc.running *= multi[cur];
          if (multi[cur] !== 100) {
            acc.total += acc.running;
            acc.running = 0;
          }
        }
        return acc;
      },
      { running: 0, total: 0 }
    );
  return result.total + result.running;
}
