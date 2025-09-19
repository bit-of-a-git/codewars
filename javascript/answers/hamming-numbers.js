function hamming(n) {
  if (!Number.isInteger(n) || n <= 0)
    throw new Error('Must be a positive integer.');

  const results = new Array(n);
  results[0] = 1;

  let i2 = 0;
  let i3 = 0;
  let i5 = 0;

  let next2 = 2;
  let next3 = 3;
  let next5 = 5;

  for (let i = 1; i < n; i += 1) {
    results[i] = Math.min(next2, next3, next5);
    if (results[i] === next2) {
      i2 += 1;
      next2 = results[i2] * 2;
    }
    if (results[i] === next3) {
      i3 += 1;
      next3 = results[i3] * 3;
    }
    if (results[i] === next5) {
      i5 += 1;
      next5 = results[i5] * 5;
    }
  }
  return results[n - 1];
}

hamming(6);
