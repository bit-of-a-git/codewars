function XO(str) {
  return [...str.matchAll(/o/gi)].length === [...str.matchAll(/x/gi)].length;
}

function XO2(str) {
  const xs = str.match(/x/gi);
  const os = str.match(/o/gi);
  return (xs && xs.length) === (os && os.length);
}
