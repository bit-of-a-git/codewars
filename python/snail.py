

def snail(snail_map: list[list]) -> list:
    result = []
    # Top
    while snail_map:
        result.extend(snail_map.pop(0))

        # Right side
        for row in snail_map:
            if row:
                result.append(row.pop(-1))

        # Bottom
        if snail_map:
            result.extend(snail_map.pop(-1)[::-1])

        # Left side
        for row in reversed(snail_map):
            if row:
                result.append(row.pop(0))

    return result

