function isPP(n) {
  if (n < 4) return null;

  // The biggest number we should check is the square root of n.
  const maxNum = Math.floor(Math.sqrt(n));

  for (let num = 2; num <= maxNum; num += 1) {
    // We start off squaring the number, and we use power to keep track
    let result = num * num;
    let power = 2;
    while (result <= n) {
      if (result === n) return [num, power];
      result *= num;
      power += 1;
    }
  }
  return null;
}
