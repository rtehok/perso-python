from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        age_score_pair = [(0, 0)] * n
        for i in range(n):
            age_score_pair[i] = (ages[i], scores[i])

        age_score_pair.sort()  # sort by age, then by score

        dp = [0] * n  # The dp[i] represents the maximum score possible by taking ith player and possible players before it

        res = 0

        for i in range(n):
            dp[i] = age_score_pair[i][1]

        for i in range(n):
            for j in range(i - 1, -1, -1):
                if age_score_pair[i][1] >= age_score_pair[j][1]:
                    dp[i] = max(dp[i], age_score_pair[i][1] + dp[j])
            res = max(res, dp[i])

        return res


if __name__ == "__main__":
    assert Solution().bestTeamScore(scores=[1, 3, 5, 10, 15], ages=[1, 2, 3, 4, 5]) == 34
    assert Solution().bestTeamScore(scores=[4, 5, 6, 5], ages=[2, 1, 2, 1]) == 16
    assert Solution().bestTeamScore(scores=[1, 2, 3, 5], ages=[8, 9, 10, 1]) == 6
