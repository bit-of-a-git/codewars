// This question limits users to Node v8.1.3, which does not have BigInt or at().

function add(a, b) {
  // maxLen is used to pad strings with 0s to avoid NaN errors, and used in the for loop
  const maxLen = Math.max(a.length, b.length);

  // We turn a and b into reverse arrays so we can iterate through them and add digits
  const revA = a.padStart(maxLen, '0').split('').reverse();
  const revB = b.padStart(maxLen, '0').split('').reverse();

  // acc holds both the result so far and digits we need to carry. E.g. 9+9 => carry: 1, result: '8'
  const acc = { carry: 0, result: '' };

  for (let i = 0; i < maxLen; i += 1) {
    const sum = acc.carry + Number(revA[i]) + Number(revB[i]);
    acc.carry = Math.floor(sum / 10);
    acc.result = (sum % 10).toString() + acc.result;
  }
  // If there is anything left over, we add to the result string
  if (acc.carry) {
    acc.result = acc.carry.toString() + acc.result;
  }
  return acc.result;
}
