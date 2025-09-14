def get_count(sentence):
    return sum(1 for ch in sentence if ch in "aeiou")
