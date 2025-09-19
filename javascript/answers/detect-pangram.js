function isPangram(string) {
  const cleanedString = string.toLowerCase().replace(/[^a-z]/g, '');
  return [...new Set(cleanedString)].length === 26;
}
