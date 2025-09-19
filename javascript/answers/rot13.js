function rot13(str) {
  return str.replace(
    /[A-Z]/gi,
    (c) =>
      'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'[
        'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'.indexOf(c)
      ]
  );
}
