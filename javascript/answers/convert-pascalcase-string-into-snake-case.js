function toUnderscore(string) {
  return string
    .split(/(?=[A-Z])/g)
    .join('_')
    .toLowerCase();
}
