from typing import List


class Solution:
    def mostPointsRec(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = {}

        def solve(index):
            if index >= n:
                return 0

            if index in memo:
                return memo[index]

            point, skip = questions[index]
            memo[index] = max(solve(index + 1), point + solve(index + skip + 1))

            return memo[index]

        return solve(0)

    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            point, skip = questions[i]
            next_question = min(n, i + skip + 1)

            dp[i] = max(dp[i + 1], point + dp[next_question])

        return dp[0]


if __name__ == "__main__":
    assert Solution().mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]) == 5
    assert Solution().mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 7
