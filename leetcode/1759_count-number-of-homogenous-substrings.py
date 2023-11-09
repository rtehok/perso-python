class Solution:
    def countHomogenousV1(self, s: str) -> int:
        sorted(s)
        prefix = []
        prefix.append(1)
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                prefix.append(prefix[i - 1] + 1)
            else:
                prefix.append(1)
        return sum(prefix) % (10 ** 9 + 7)

    def countHomogenous(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        curr_streak = 0
        ans = 0
        for i in range(len(s)):
            if i == 0 or s[i] == s[i - 1]:
                curr_streak += 1
            else:
                curr_streak = 1

            ans += curr_streak
            ans %= MOD

        return ans


if __name__ == "__main__":
    assert Solution().countHomogenous("abbcccaa") == 13
    assert Solution().countHomogenous("xy") == 2
    assert Solution().countHomogenous("zzzzz") == 15
