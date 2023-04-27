class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_length = 0
        start = 0

        chars = {}

        for i, c in enumerate(s):
            if c in chars.keys():
                start = max(start, chars[c] + 1)  # move start after repeated char

            chars[c] = i
            max_length = max(max_length, i - start + 1)

        return max_length


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    assert Solution().lengthOfLongestSubstring("abba") == 2
    assert Solution().lengthOfLongestSubstring("dvdf") == 3
