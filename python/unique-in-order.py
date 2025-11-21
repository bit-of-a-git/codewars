def unique_in_order(sequence: list):
    result = []

    for i in range(1, len(sequence) - 1):
        if sequence[i] != sequence[i-1]:
            result.append(sequence[i])
    return result

if __name__ == "__main__":
    print(unique_in_order([1, 2]))