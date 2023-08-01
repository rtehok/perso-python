import collections


class Solution:
    def minimumDeleteSumV1(self, s1: str, s2: str) -> int:
        def compute_cost(i, j):
            if i < 0:
                delete_cost = 0
                for x in range(j + 1):
                    delete_cost += ord(s2[x])
                return delete_cost

            if j < 0:
                delete_cost = 0
                for x in range(i + 1):
                    delete_cost += ord(s1[x])
                return delete_cost

            if s1[i] == s2[j]:
                return compute_cost(i - 1, j - 1)
            else:
                return min(
                    ord(s1[i]) + compute_cost(i - 1, j),
                    ord(s2[j]) + compute_cost(i, j - 1),
                    ord(s1[i]) + ord(s2[j]) + compute_cost(i - 1, j - 1)
                )

        return compute_cost(len(s1) - 1, len(s2) - 1)

    def minimumDeleteSumTopDown(self, s1: str, s2: str) -> int:
        memo = collections.defaultdict(int)

        def compute_cost(i, j):
            if i < 0 and j < 0:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if i < 0:
                memo[(i, j)] = ord(s2[j]) + compute_cost(i, j - 1)
                return memo[(i, j)]

            if j < 0:
                memo[(i, j)] = ord(s1[i]) + compute_cost(i - 1, j)
                return memo[(i, j)]

            if s1[i] == s2[j]:
                return compute_cost(i - 1, j - 1)
            else:
                memo[(i, j)] = min(
                    ord(s1[i]) + compute_cost(i - 1, j),
                    ord(s2[j]) + compute_cost(i, j - 1)
                )

            return memo[(i, j)]

        return compute_cost(len(s1) - 1, len(s2) - 1)

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        ord(s1[i - 1]) + dp[i - 1][j],
                        ord(s2[j - 1]) + dp[i][j - 1]
                    )

        return dp[-1][-1]


if __name__ == "__main__":
    assert Solution().minimumDeleteSum(s1="sea", s2="eat") == 231
    assert Solution().minimumDeleteSum(s1="delete", s2="leet") == 403
