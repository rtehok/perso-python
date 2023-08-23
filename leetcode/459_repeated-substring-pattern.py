class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for i in range(1, n // 2 + 1):
            if n % i == 0:
                pattern = s[:i] * (n // i)
                if s == pattern:
                    return True

        return False


if __name__ == "__main__":
    assert Solution().repeatedSubstringPattern("abab")
    assert not Solution().repeatedSubstringPattern("aba")
    assert Solution().repeatedSubstringPattern("abcabcabcabc")
