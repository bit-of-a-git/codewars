from typing import List


class Solution:
    def maxFrequencyElementsNaive(self, nums: List[int]) -> int:
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        max_frequency = max(frequencies.values())
        count = 0
        for num in nums:
            if frequencies[num] == max_frequency:
                count += 1
        return count

    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencies = {}
        max_frequency = 0
        total_frequencies = 0

        # Just one loop
        for num in nums:
            count = frequencies.get(num, 0) + 1
            frequencies[num] = count
            if count > max_frequency:
                max_frequency = count
                total_frequencies = count
            elif count == max_frequency:
                total_frequencies += count
        return total_frequencies
