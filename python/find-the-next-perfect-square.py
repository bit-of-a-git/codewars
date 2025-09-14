def find_next_square(sq: int):
    # Return the next square if sq is a square, -1 otherwise
    root = sq**0.5
    if root.is_integer():
        return (root + 1) ** 2
    return -1
