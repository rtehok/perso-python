class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}

        cnt_vowels = 0

        for i in range(k):
            if s[i] in vowels:
                cnt_vowels += 1

        max_vowels = cnt_vowels

        for i in range(k, len(s)):
            if max_vowels == k:
                return k
            cnt_vowels += 1 if s[i] in vowels else 0
            cnt_vowels -= 1 if s[i - k] in vowels else 0
            max_vowels = max(max_vowels, cnt_vowels)

        return max_vowels


if __name__ == "__main__":
    assert Solution().maxVowels(s="tnfazcwrryitgacaabwm", k=4) == 3
    assert Solution().maxVowels(s="pdzndkhhoujpqyex", k=5) == 2
    assert Solution().maxVowels(s="leetcode", k=3) == 2
    assert Solution().maxVowels(s="abciiidef", k=3) == 3
    assert Solution().maxVowels(s="aeiou", k=2) == 2
