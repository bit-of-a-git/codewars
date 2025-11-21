def alphabet_position(text):
    result = []
    for letter in text:
        if str.isalpha(letter):
            number = ord(letter.lower())
            number = number - 96
            result.append(str(number))
    return " ".join(result)
