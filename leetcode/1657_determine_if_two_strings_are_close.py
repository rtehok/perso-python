from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and sorted(Counter(word1).values()) == sorted(Counter(word2).values())


if __name__ == "__main__":
    assert Solution().closeStrings(word1="abc", word2="bca")
    assert not Solution().closeStrings(word1="a", word2="aa")
    assert Solution().closeStrings(word1="cabbba", word2="abbccc")
