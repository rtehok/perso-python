import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        for v in collections.Counter(s).values():
            res += v // 2 * 2  # if v is odd, set to leftmost even number

            if v % 2 == 1 and res % 2 == 0:  # add to center if not already there
                res += 1

        return res


if __name__ == "__main__":
    assert Solution().longestPalindrome("abccccdd") == 7
    assert Solution().longestPalindrome("a") == 1
