def kSubNaive(k, nums):
    numsLen = len(nums)
    kCount = 0
    for i in range(numsLen):
        for j in range(i, numsLen):
            if sum(nums[i : j + 1]) % k == 0:
                kCount += 1
    return kCount


def kSubImproved(k, nums):
    numsLen = len(nums)
    kCount = 0
    for i in range(numsLen):
        # We change to a total as sum() is O(n)
        total = 0
        for j in range(i, numsLen):
            total += nums[j]
            if total % k == 0:
                kCount += 1
    return kCount
