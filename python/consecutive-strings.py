def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    longest = strarr[0:k]
    for i in range(1, n - k + 1):
        candidate = strarr[i : i + k]
        if sum(len(s) for s in candidate) > sum(len(s) for s in longest):
            longest = candidate
    return "".join(longest)
