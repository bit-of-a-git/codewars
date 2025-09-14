def solution(s):
    # return [s[i : i + 2].ljust(2, "_") for i in range(0, len(s), 2)]
    result = []
    for i in range(0, len(s), 2):
        pair = s[i : i + 2].ljust(2, "_")
        result.append(pair)
    return result
