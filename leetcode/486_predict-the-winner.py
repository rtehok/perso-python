import collections
from typing import List


class Solution:
    # TC O(2 ** n) / SC O(n)
    def PredictTheWinnerRecursive(self, nums: List[int]) -> bool:
        n = len(nums)

        def maxDiff(left, right):
            if left == right:
                return nums[left]

            score_by_left = nums[left] - maxDiff(left + 1, right)
            score_by_right = nums[right] - maxDiff(left, right - 1)
            return max(score_by_left, score_by_right)

        return maxDiff(0, n - 1) >= 0

    def PredictTheWinnerRecursionWithMemo(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = collections.defaultdict(int)

        def maxDiff(left, right):
            if (left, right) in memo:
                return memo[(left, right)]

            if left == right:
                return nums[left]

            score_by_left = nums[left] - maxDiff(left + 1, right)
            score_by_right = nums[right] - maxDiff(left, right - 1)

            memo[(left, right)] = max(score_by_left, score_by_right)
            return memo[(left, right)]

        return maxDiff(0, n - 1) >= 0

    def PredictTheWinnerBottomUp(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                dp[left][right] = max(nums[left] - dp[left + 1][right], nums[right] - dp[left][right - 1])

        return dp[0][-1] >= 0

    # TC O(n**2) / SC O(n)
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:]

        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                dp[left] = max(nums[left] - dp[left + 1], nums[right] - dp[left])

        return dp[0] >= 0


if __name__ == "__main__":
    assert not Solution().PredictTheWinner([1, 5, 2])
    assert Solution().PredictTheWinner([1, 5, 233, 7])
