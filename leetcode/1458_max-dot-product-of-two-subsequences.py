import functools
from typing import List


class Solution:
    def maxDotProductTopDown(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        @functools.cache
        def dp(i, j):
            if i == m or j == n:
                return 0

            ans = nums1[i] * nums2[j] + dp(i + 1, j + 1)
            return max(ans, dp(i + 1, j), dp(i, j + 1))

        if max(nums1) < 0 < min(nums2):
            return max(nums1) * min(nums2)

        if min(nums1) > 0 > max(nums2):
            return min(nums1) * max(nums2)

        return dp(0, 0)

    def maxDotProductBottomUp(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                ans = nums1[i] * nums2[j] + dp[i + 1][j + 1]
                dp[i][j] = max(ans, dp[i + 1][j], dp[i][j + 1])

        if max(nums1) < 0 < min(nums2):
            return max(nums1) * min(nums2)

        if min(nums1) > 0 > max(nums2):
            return min(nums1) * max(nums2)

        return dp[0][0]

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        dp = [0] * (n + 1)
        dp_prev = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            dp = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                ans = nums1[i] * nums2[j] + dp_prev[j + 1]
                dp[j] = max(ans, dp_prev[j], dp[j + 1])

            dp_prev = dp

        if max(nums1) < 0 < min(nums2):
            return max(nums1) * min(nums2)

        if min(nums1) > 0 > max(nums2):
            return min(nums1) * max(nums2)

        return dp[0]


if __name__ == "__main__":
    assert Solution().maxDotProduct(nums1=[2, 1, -2, 5], nums2=[3, 0, -6]) == 18
    assert Solution().maxDotProduct(nums1=[3, -2], nums2=[2, -6, 7]) == 21
    assert Solution().maxDotProduct(nums1=[-1, -1], nums2=[1, 1]) == -1
