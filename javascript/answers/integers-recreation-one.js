function listSquared(m, n) {
  const result = [];
  for (let i = m; i <= n; i += 1) {
    // We start with 1 and the number itself
    const divisors = new Set([1, i]);
    // We go as far as the square root, as by that point we have all the divisors
    const sqrt = Math.sqrt(i);
    // We start with 2, as we have already covered 1
    for (let d = 2; d <= sqrt; d += 1) {
      if (i % d === 0) {
        // We add both the divisor and the result
        divisors.add(d);
        divisors.add(i / d);
      }
    }
    const sumOfSquares = [...divisors].reduce((acc, cur) => acc + cur * cur, 0);

    if (sumOfSquares && Number.isInteger(Math.sqrt(sumOfSquares))) {
      result.push([i, sumOfSquares]);
    }
  }
  return result;
}
