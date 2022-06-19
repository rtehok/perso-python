from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        d = {}
        res = 1

        for word in sorted(words, key=len):
            d[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                if prev in d.keys():
                    d[word] = max(d[prev] + 1, d[word])
                    res = max(res, d[word])

        return res


if __name__ == "__main__":
    assert Solution().longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]) == 4
    assert Solution().longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) == 5
    assert Solution().longestStrChain(["abcd", "dbqca"]) == 1
    assert Solution().longestStrChain(["c", "cd", "ab", "bcd", "abc", "abcd", "abcde"]) == 5
