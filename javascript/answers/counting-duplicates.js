function duplicateCount(text) {
  const normalised = text.toLowerCase();
  const counts = {};
  normalised.split('').forEach((char) => {
    counts[char] = (counts[char] || 0) + 1;
  });
  return Object.values(counts).filter((i) => i > 1).length;
}
