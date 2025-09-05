function maskify(cc) {
  return '#'.repeat(Math.max(0, cc.length - 4)) + cc.slice(-4);
}
