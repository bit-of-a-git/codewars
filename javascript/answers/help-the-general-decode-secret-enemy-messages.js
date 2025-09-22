device.decode = function (w) {
  return w
    .split('')
    .map((a, i) => {
      return device.encode('_'.repeat(64 - i) + a)[64 - i];
    })
    .join('');
};
