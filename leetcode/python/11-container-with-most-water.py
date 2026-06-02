from typing import List


class Solution:
    def maxAreaNaive(self, height: List[int]) -> int:
        result = 0

        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                water = (min(height[i], height[j])) * (j - i)
                result = max(result, water)
        return result

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            x = min(height[left], height[right])
            y = right - left
            water = x * y
            result = max(result, water)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return result
