class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = [0] * 26

        for i in range(len(s)):
            cnt[ord(t[i]) - ord('a')] += 1
            cnt[ord(s[i]) - ord('a')] -= 1

        return sum(max(0, c) for c in cnt)


assert Solution().minSteps("bab", "aba") == 1
assert Solution().minSteps("leetcode", "practice") == 5
assert Solution().minSteps("anagram", "mangaar") == 0
