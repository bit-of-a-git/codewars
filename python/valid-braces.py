def valid_braces(string):
    stack = []
    openToClose = {
        "(": ")",
        "[": "]",
        "{": "}",
    }

    for c in string:
        if c in openToClose:
            stack.append(c)
        else:
            if stack and (c == openToClose[stack[-1]]):
                stack.pop()
            else:
                return False
    return False if stack else True
