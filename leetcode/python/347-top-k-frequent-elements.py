from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [num for num, _ in counter.most_common(k)]

    def topKFrequentSecondGo(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1

        # We need to sort by value, in reverse
        # We use .items() to get access to the values
        sortedItems = sorted(freqMap.items(), key=lambda x: x[1], reverse=True)

        # sortedItems is a list of tuples. We unpack them and discard the second item
        return [num for num, _ in sortedItems[:k]]

    def topKFrequentFirstGo(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1

        sortedMap = dict(sorted(freqMap.items(), key=lambda x: x[1], reverse=True))
        return list(sortedMap)[:k]
