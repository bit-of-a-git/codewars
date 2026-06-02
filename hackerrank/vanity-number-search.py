#
# Complete the 'vanity' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY codes
#  2. STRING_ARRAY numbers
#

numMap = {
    "A": "2",
    "B": "2",
    "C": "2",
    "D": "3",
    "E": "3",
    "F": "3",
    "G": "4",
    "H": "4",
    "I": "4",
    "J": "5",
    "K": "5",
    "L": "5",
    "M": "6",
    "N": "6",
    "O": "6",
    "P": "7",
    "Q": "7",
    "R": "7",
    "S": "7",
    "T": "8",
    "U": "8",
    "V": "8",
    "W": "9",
    "X": "9",
    "Y": "9",
    "Z": "9",
}


def vanity(codes, numbers):
    # We use a set to hold our unique numbers
    result = set()
    for code in codes:
        convertedCode = []
        # We get the number value for each character in the code
        for c in code:
            convertedCode.append(numMap[c])
        convertedCode = "".join(convertedCode)
        # We then check whether the code appears in a number
        for number in numbers:
            if convertedCode in number and number not in result:
                result.add(number)
    return sorted(result)
