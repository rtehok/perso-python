class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1

        while left < right and s[left] == s[right]:
            c = s[left]
            while left <= right and s[left] == s[right]:
                left += 1

            while right > left and s[right] == c:
                right -= 1

        return right - left + 1


assert Solution().minimumLength("ca") == 2
assert Solution().minimumLength("cabaabac") == 0
assert Solution().minimumLength("aabccabba") == 3
assert Solution().minimumLength("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb") == 1