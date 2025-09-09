function countSmileys(arr) {
  return arr.filter((s) => /^[:;][-~]?[)D]$/.test(s)).length;
}
