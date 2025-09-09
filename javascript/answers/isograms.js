function isIsogram(str) {
  const s = str.toLowerCase();
  return new Set(s).size === s.length;
}
