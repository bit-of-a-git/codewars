class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}
        for c in magazine:
            mag_dict[c] = 1 + mag_dict.get(c, 0)

        for c in ransomNote:
            if c not in mag_dict or mag_dict[c] <= 0:
                return False
            mag_dict[c] -= 1

        return True
