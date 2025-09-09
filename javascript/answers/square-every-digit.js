function squareDigits(num) {
  return Number(
    String(num)
      .split('')
      .map((i) => Number(i) ** 2)
      .join('')
  );
}
