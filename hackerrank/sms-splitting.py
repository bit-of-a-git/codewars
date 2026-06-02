import math


def segmentsFirstGo(message):
    messageLen = len(message)
    if messageLen <= 160:
        return [message]
    # An SMS can be 160 characters, but we know our suffix will always be 5
    smsLength = 160 - 5
    segmentCount = math.ceil(len(message) / smsLength)

    result = []
    for i in range(segmentCount):
        start = smsLength * i
        end = smsLength * (i + 1)
        msg = message[start:end]
        suffix = f"({i + 1}/{segmentCount})"
        result.append(f"{msg}{suffix}")
    return result
