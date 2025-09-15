def first_non_repeating_letter(s: str):
    print(s)
    for char in s:
        if s.lower().count(char.lower()) == 1:
            return char
    return ""
