class Solution:
    def numberOfArraysRecursive(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(s), len(str(k))

        dp = [0] * (m + 1)

        def dfs(start):
            if dp[start]:
                return dp[start]

            if start == m:
                return 1

            if s[start] == '0':
                return 0

            # For all possible starting number, add the number of arrays
            # that can be printed as the remaining string to count.

            count = 0

            for end in range(start, m):
                current_number = int(s[start: end + 1])
                if current_number > k:
                    break

                count += dfs(end + 1)

            dp[start] = count % MOD
            return count

        return dfs(0) % MOD

    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)

        # dp[i] records the number of arrays that can be printed as
        # the prefix substring s[0 ~ i - 1]
        dp = [0] * (n + 1)

        dp[0] = 1  # one way to form an array of 0 characters

        for start in range(n):
            if s[start] == '0':
                continue

            for end in range(start, n):
                current_number = int(s[start: end + 1])
                if current_number > k:
                    break

                dp[end + 1] += dp[start]
                dp[end + 1] %= MOD

        return dp[-1]


if __name__ == "__main__":
    assert Solution().numberOfArrays(s="1307", k=2000) == 4
    assert Solution().numberOfArrays(s="1000", k=10000) == 1
    assert Solution().numberOfArrays(s="1317", k=2000) == 8
    assert Solution().numberOfArrays(s="1000", k=10) == 0
