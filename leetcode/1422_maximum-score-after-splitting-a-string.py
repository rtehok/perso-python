class Solution:
    def maxScoreV1(self, s: str) -> int:
        n = len(s)
        prefix_zeros = [0] * n
        suffix_ones = [0] * n

        prefix_zeros[0] = 1 if s[0] == "0" else 0
        suffix_ones[-1] = 1 if s[-1] == "1" else 0

        for i in range(1, n - 1):
            if s[i] == "0":
                prefix_zeros[i] = prefix_zeros[i - 1] + 1
            else:
                prefix_zeros[i] = prefix_zeros[i - 1]

        for i in range(n - 2, 0, -1):
            if s[i] == "1":
                suffix_ones[i] = suffix_ones[i + 1] + 1
            else:
                suffix_ones[i] = suffix_ones[i + 1]

        max_score = 0
        for i in range(n - 1):
            max_score = max(max_score, prefix_zeros[i] + suffix_ones[i + 1])

        return max_score

    def maxScore(self, s: str) -> int:
        ones = 0
        zeros = 0
        best = float("-inf")

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones += 1
            else:
                zeros += 1

            best = max(best, zeros - ones)

        if s[-1] == "1":
            ones += 1

        return best + ones


assert Solution().maxScore("01") == 2
assert Solution().maxScore("00") == 1
assert Solution().maxScore("1111") == 3
assert Solution().maxScore("011101") == 5
assert Solution().maxScore("00111") == 5
