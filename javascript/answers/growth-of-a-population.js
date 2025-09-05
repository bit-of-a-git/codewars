function nbYear(p0, percent, aug, p) {
  let n = 0;
  let population = p0;
  while (population < p) {
    population = Math.floor(population * (1 + percent / 100) + aug);
    n += 1;
  }
  return n;
}
