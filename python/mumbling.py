def accum(st):
    return "-".join(ch.upper() + ch.lower() * i for i, ch in enumerate(st))
