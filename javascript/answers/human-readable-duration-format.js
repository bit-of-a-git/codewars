function formatDuration(seconds) {
  if (seconds === 0) return 'now';
  let remainingSeconds = seconds;
  const res = [];
  const units = {
    year: 365 * 24 * 60 * 60,
    day: 24 * 60 * 60,
    hour: 60 * 60,
    minute: 60,
    second: 1,
  };
  Object.entries(units).forEach(([unit, size]) => {
    if (remainingSeconds >= size) {
      const value = Math.floor(remainingSeconds / size);
      res.push(`${value} ${unit}${value > 1 ? 's' : ''}`);
      remainingSeconds %= size;
    }
  });
  return res.join(', ').replace(/,([^,]*)$/, ' and$1');
}
