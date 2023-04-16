from typing import List


class Solution:
    def numWaysTLE(self, words: List[str], target: str) -> int:
        d = {}

        for i, word in enumerate(words):
            for j, c in enumerate(word):
                if c not in d:
                    d[c] = [[] for _ in range(len(words))]
                    d[c][i] = [j]
                else:
                    d[c][i].append(j)

        res = 0

        def helper(prev, letter_index, length):
            nonlocal res

            if length == len(target):
                res += 1
                return

            if target[letter_index] not in d:
                return

            for indices in d[target[letter_index]]:
                for index in indices:
                    if index > prev:
                        helper(index, letter_index + 1, length + 1)

        helper(-1, 0, 0)

        return res

    def numWays(self, words: List[str], target: str) -> int:
        mod = 10 ** 9 + 7
        m = len(target)
        k = len(words[0])
        cnt = [[0] * k for _ in range(26)]
        for j in range(k):
            for word in words:
                cnt[ord(word[j]) - ord('a')][j] += 1

        dp = [[0] * (k + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for i in range(m + 1):
            for j in range(k):
                if i < m:
                    dp[i + 1][j + 1] += (cnt[ord(target[i]) - ord('a')][j]) * dp[i][j]
                    dp[i + 1][j + 1] %= mod
                dp[i][j + 1] += dp[i][j]
                dp[i][j + 1] %= mod
        return dp[m][k]


if __name__ == "__main__":
    assert Solution().numWays(words=["acca", "bbbb", "caca"], target="aba") == 6
    assert Solution().numWays(words=["abba", "baab"], target="bab") == 4
    assert Solution().numWays(words=["ddcc", "bdcb", "bdbb"], target="bab") == 0
