function score(dice) {
  const scores = {
    111: 1000,
    666: 600,
    555: 500,
    444: 400,
    333: 300,
    222: 200,
    1: 100,
    5: 50,
  };
  let sum = 0;
  // No toSorted() in the Node version being used for this challenge
  // Instead we make a shallow copy and sort in ascending order
  const sortedDice = dice.slice().sort((a, b) => a - b);
  for (let i = 0; i < sortedDice.length - 2; i += 1) {
    if (
      sortedDice[i] === sortedDice[i + 1] &&
      sortedDice[i] === sortedDice[i + 2]
    ) {
      sum += scores[sortedDice.slice(i, i + 3).join('')] || 0;
      // We remove the triples so they are not double-counted, and bring the index back so that we do not miss any array element that has been shifted left
      sortedDice.splice(i, 3);
      i -= 1;
    }
  }
  sortedDice.forEach((element) => {
    sum += scores[element] || 0;
  });
  return sum;
}
