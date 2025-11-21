function solution(string) {
  return string.replace(/(?=[A-Z])/g, ' ');
}

function solution2(string) {
  return string
    .split('')
    .map((a) => (a === a.toUpperCase() ? `_${a}` : a))
    .join('');
}
