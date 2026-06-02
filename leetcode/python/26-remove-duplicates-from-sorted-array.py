from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numsLen = len(nums)
        # We use left to write unique elements
        # We will never write to 0, so we initialise it to 1
        left = 1

        # We use right to check for duplicates
        # Since the array is sorted, we compare the element
        # at right to the one that comes before it.
        # If they differ, we know the element at right
        # is a new unique one and we write it.

        for right in range(1, numsLen):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1

        # Left will always be the position of the next writing position
        # That means it is always equal to the number of unique elements
        return left
