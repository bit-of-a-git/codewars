def generate_hashtag(s: str):
    if s.strip() == "" or len(s.replace(" ", "")) >= 140:
        return False
    result = "#" + "".join(word.capitalize() for word in s.split())
    return result
