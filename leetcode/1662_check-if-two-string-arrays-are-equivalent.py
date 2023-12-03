from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)


if __name__ == "__main__":
    assert Solution().arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"])
    assert not Solution().arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"])
    assert Solution().arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddefg"])
