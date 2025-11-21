def duplicate_encode(word: str):
    result = ""
    for i in word.lower():
        if word.lower().count(i) > 1:
            result += ")"
        else:
            result += "("
    return result

def duplicate_encode_2(word: str):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
