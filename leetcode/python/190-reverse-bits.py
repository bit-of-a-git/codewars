class Solution:
    # Explanation:
    # 1. We convert n to binary
    # 2. Remove 0b
    # 3. Pad the start to 32 bytes if needed
    # 4. Reverse
    # 5. Convert back to an int
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)
