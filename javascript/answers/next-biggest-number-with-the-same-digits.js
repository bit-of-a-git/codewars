function nextBigger(n) {
  // We split the number into an array so we can iterate through them
  const arr = n.toString().split('').map(Number);

  let pivot = -1;
  let nextGreater;

  for (let i = arr.length - 1; i > 0; i -= 1) {
    if (arr[i - 1] < arr[i]) {
      pivot = i - 1;
      break;
    }
  }
  if (pivot < 0) return -1;

  for (let j = arr.length - 1; j > pivot; j -= 1) {
    if (arr[j] > arr[pivot]) {
      nextGreater = j;
      break;
    }
  }

  [arr[pivot], arr[nextGreater]] = [arr[nextGreater], arr[pivot]];
  return Number(
    [...arr.slice(0, pivot + 1), ...arr.slice(pivot + 1).reverse()].join('')
  );
}
