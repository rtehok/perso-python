import collections
from typing import List


class Solution:
    def validPartitionTopDown(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {-1: True}

        def dfs(i):
            if i in memo:
                return memo[i]

            ans = False

            if i > 0 and nums[i] == nums[i - 1]:
                ans |= dfs(i - 2)

            if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
                ans |= dfs(i - 3)

            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:
                ans |= dfs(i - 3)

            memo[i] = ans

            return memo[i]

        return dfs(n - 1)

    def validPartitionBottomUp(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n):
            dp_index = i + 1
            if i > 0 and nums[i] == nums[i - 1]:
                dp[dp_index] |= dp[dp_index - 2]

            if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
                dp[dp_index] |= dp[dp_index - 3]

            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:
                dp[dp_index] |= dp[dp_index - 3]

        return dp[-1]

    def validPartitionBottomUpOptimized(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * 3
        dp[0] = True

        for i in range(n):
            dp_index = i + 1
            ans = False
            if i > 0 and nums[i] == nums[i - 1]:
                ans |= dp[(dp_index - 2) % 3]

            if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
                ans |= dp[(dp_index - 3) % 3]

            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:
                ans |= dp[(dp_index - 3) % 3]

            dp[dp_index % 3] = ans

        return dp[n % 3]

    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        q = collections.deque([0])

        seen = set()

        while q:
            i = q.popleft()

            if i == n:
                return True

            if i + 1 < n and nums[i] == nums[i + 1] and i + 2 not in seen:
                seen.add(i + 2)
                q.append(i + 2)

            if i + 2 < n and (nums[i] == nums[i + 1] == nums[i + 2] or nums[i] == nums[i + 1] - 1 == nums[i + 2] - 2) and i + 3 not in seen:
                seen.add(i + 3)
                q.append(i + 3)

        return False


if __name__ == "__main__":
    assert Solution().validPartition([4, 4, 4, 5, 6])
    assert not Solution().validPartition([1, 1, 1, 2])
