function generateHashtag(str) {
  if (!str.trim()) return false;
  const returnString = str
    .split(/\s+/)
    .reduce((a, c) => a + c.charAt(0).toUpperCase() + c.slice(1), '#');
  if (returnString.length > 140) {
    return false;
  }
  return returnString;
}
