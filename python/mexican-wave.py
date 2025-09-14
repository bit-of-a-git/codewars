def wave(people):
    newArr = []
    for i, ch in enumerate(people):
        if ch.isalpha():
            waved = people[:i] + ch.upper() + people[i + 1 :]
            newArr.append(waved)
    return newArr


if __name__ == "__main__":
    result = wave("h e l l o")
    print(result)
