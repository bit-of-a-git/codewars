let uniqueInOrder = function (iterable) {
  return Array.from(iterable).filter((el, ind, arr) => el !== arr[ind + 1]);
};
