class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N = len(needle)

        if len(needle) > len(haystack):
            return -1
        if needle == haystack:
            return 0

        for i in range(len(haystack)):
            if i <= len(haystack) - N and haystack[i:i + N] != needle:
                continue
            if haystack[i:i + N] == needle:
                return i
        return -1


if __name__ == "__main__":
    assert Solution().strStr("hello", "ll") == 2
    assert Solution().strStr("aaaaa", "bba") == -1
    assert Solution().strStr("a", "a") == 0
    assert Solution().strStr("abc", "c") == 2
