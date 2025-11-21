// First go
function alphabetPosition(text) {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  return text
    .toLowerCase()
    .split('')
    .filter((a) => alphabet.includes(a))
    .map((a) => alphabet.indexOf(a) + 1)
    .join(' ');
}

// Second go
function alphabetPosition2(text) {
  return text
    .toLowerCase()
    .replace(/[^a-z]/g, '')
    .split('')
    .map((a) => a.charCodeAt(0) - 96)
    .join(' ');
}
