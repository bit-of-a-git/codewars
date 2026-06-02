class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We initialise a set to hold unique characters
        charSet = set()
        left = 0
        result = 0

        for right in range(len(s)):
            # If right is in the charSet, we keep removing
            # from the left until it is removed
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            result = max(result, right - left + 1)
        return result
