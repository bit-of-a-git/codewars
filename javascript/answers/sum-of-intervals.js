function isOverlapping(a, b) {
  // What this is really doing is selecting the biggest starting number of the ranges, in this case 3
  // And comparing it to the smallest ending number of the ranges, in this case 4
  // For a pair like [1,5] and [6,10] -> is 6 < 5? No, so they are not overlapping
  return Math.max(a[0], b[0]) < Math.min(a[1], b[1]);
}

function sumIntervals(arr) {
  // Create a deep copy of the input array to avoid mutating the parameter
  const intervals = arr.map((interval) => interval.slice());

  // How do we know if an array overlaps?
  // [1, 4] and [3, 5] do
  // Basically if any of the numbers in between the second exist in the first
  for (let i = 0; i < intervals.length - 1; i += 1) {
    for (let j = i + 1; j < intervals.length; j += 1)
      if (isOverlapping(intervals[i], intervals[j])) {
        intervals[i][0] = Math.min(intervals[i][0], intervals[j][0]);
        intervals[i][1] = Math.max(intervals[i][1], intervals[j][1]);
        intervals.splice(j, 1);
      }
  }

  return intervals.reduce((acc, cur) => acc + (cur[1] - cur[0]), 0);
}
