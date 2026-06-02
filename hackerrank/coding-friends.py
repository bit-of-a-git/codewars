def minNum(samDaily, kellyDaily, difference):
    # if Sam solves the same or more problems than Kelly, she cannot surpass his count
    if samDaily >= kellyDaily:
        return -1
    else:
        # We get the days by doing floor divison and adding 1
        return difference // (kellyDaily - samDaily) + 1
