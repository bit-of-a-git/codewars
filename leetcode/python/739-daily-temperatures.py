from typing import List


class Solution:
    def dailyTemperaturesNaive(self, temperatures: List[int]) -> List[int]:
        resultArr = []
        # We need to check each of the elements
        for i in range(len(temperatures)):
            # We set days to 0 so that if none is found, 0 is appended
            days = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    days = j - i
                    break
            resultArr.append(days)
        return resultArr
