class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)

        for c in word:
            if c.isupper():
                n -= 1
        return n == 0 or n == len(word) or (word[0].isupper() and n == len(word) - 1)


if __name__ == "__main__":
    assert Solution().detectCapitalUse("USA")
    assert not Solution().detectCapitalUse("FlaG")
    assert Solution().detectCapitalUse("g")
    assert not Solution().detectCapitalUse("ffffffffffffffffffffF")
