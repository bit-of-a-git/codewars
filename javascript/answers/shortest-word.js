function findShort(s) {
  return s.split(' ').reduce((a, b) => (a.length <= b.length ? a : b)).length;
}
