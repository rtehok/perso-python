class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        ans = 0

        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()

            for k in range(i + 1, j):
                between.add(s[k])

            ans += len(between)

        return ans


if __name__ == "__main__":
    assert Solution().countPalindromicSubsequence("aabca") == 3
    assert Solution().countPalindromicSubsequence("bbcbaba") == 4
    assert Solution().countPalindromicSubsequence("adc") == 0