# First attempt
def countNumberOfSubarraysNaive(arr, k):
    result = 0
    arrLen = len(arr)
    for i in range(arrLen):
        count = 0
        for j in range(i, arrLen):
            count += arr[j]
            if count == k:
                result += 1
    return result


def countNumberOfSubarrays(arr, k):
    # This handles when arr[0] = k
    prefix_dict = {0: 1}
    result = 0
    running_count = 0

    for num in arr:
        running_count += num
        needed = running_count - k
        result += prefix_dict.get(needed, 0)
        prefix_dict[running_count] = prefix_dict.get(running_count, 0) + 1

    return result


countNumberOfSubarrays([1, 2, 3, 0], 3)
