function firstNonRepeatingLetter(s) {
  // For each letter in s
  for (let i = 0; i < s.length; i += 1) {
    if (
      // We filter s to only the characters that are the same as s[i]
      // If the length is 1, we return that character
      s
        .toLowerCase()
        .split('')
        .filter((c) => c === s[i].toLowerCase()).length === 1
    ) {
      return s[i];
    }
  }
  return '';
}
