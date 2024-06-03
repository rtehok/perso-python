class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        first = 0
        longest_prefix = 0
        while first < len(s) and longest_prefix < len(t):
            if s[first] == t[longest_prefix]:
                longest_prefix += 1
            first += 1

        return len(t) - longest_prefix


assert Solution().appendCharacters(s="coaching", t="coding") == 4
assert Solution().appendCharacters(s="abcde", t="a") == 0
assert Solution().appendCharacters(s="z", t="abcde") == 5
