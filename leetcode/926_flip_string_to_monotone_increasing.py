class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        number_of_ones = 0
        res = 0

        for c in s:
            if c == '0':
                # decide whether to switch 0 or not
                res = min(res + 1, number_of_ones)
            else:
                number_of_ones += 1

        return res


if __name__ == "__main__":
    assert Solution().minFlipsMonoIncr("00110") == 1
    assert Solution().minFlipsMonoIncr("010110") == 2
    assert Solution().minFlipsMonoIncr("00011000") == 2
