class Solution:
    def maxScore(self, s: str) -> int:
        # We initialise the count of zeros and the max_score calculated to 0
        count_zeros_left = max_score = 0
        # We get the ones in the whole string. As we progress, we
        # update the count so it always matches the ones on the right
        count_ones_right = s.count("1")

        len_s = len(s)
        # We want to stop at len - 1, as otherwise there will be no right hand side
        for i in range(len_s - 1):
            # We take advantage of True converting to 1
            count_zeros_left += s[i] == "0"
            count_ones_right -= s[i] == "1"
            # We update the max_score by comparing it with the current score
            max_score = max(max_score, count_zeros_left + count_ones_right)

        return max_score
