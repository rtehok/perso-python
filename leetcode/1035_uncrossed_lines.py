import collections
from typing import List


class Solution:
    def maxUncrossedLinesV1(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        memo = {}

        def solve(i, j):
            if i <= 0 or j <= 0:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if nums1[i - 1] == nums2[j - 1]:
                memo[(i, j)] = 1 + solve(i - 1, j - 1)
            else:
                memo[(i, j)] = max(solve(i - 1, j), solve(i, j - 1))

            return memo[(i, j)]

        return solve(n1, n2)

    def maxUncrossedLinesDP(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        dp = [0] * (len(nums2) + 1)
        for i in range(1, len(nums1) + 1):
            prev = 0
            for j in range(1, len(nums2) + 1):
                cur = dp[j]
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = cur
        return dp[len(nums2)]


if __name__ == "__main__":
    assert Solution().maxUncrossedLines(nums1=[1, 4, 2], nums2=[1, 2, 4]) == 2
    assert Solution().maxUncrossedLines(nums1=[2, 5, 1, 2, 5], nums2=[10, 5, 2, 1, 5, 2]) == 3
    assert Solution().maxUncrossedLines(nums1=[1, 3, 7, 1, 7, 5], nums2=[1, 9, 2, 5, 1]) == 2
