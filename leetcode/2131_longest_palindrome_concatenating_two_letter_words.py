import collections
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = collections.Counter(words)

        res = 0

        central = False

        for word, c in cnt.items():
            if word[0] == word[1]:
                if c % 2 == 0:
                    res += c
                else:
                    res += c - 1
                    central = True
            elif word[0] < word[1]:
                res += 2 * min(c, cnt[word[1] + word[0]])
        if central:
            res += 1

        return res * 2


if __name__ == "__main__":
    assert Solution().longestPalindrome(words=["lc", "cl", "gg"]) == 6
    assert Solution().longestPalindrome(words=["ab", "ty", "yt", "lc", "cl", "ab"]) == 8
    assert Solution().longestPalindrome(words=["cc", "ll", "xx"]) == 2
