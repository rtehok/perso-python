from typing import List


class Solution:
    # this is the fastest solution...
    def canPartitionBruteForce(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2:
            return False

        target_sum = total_sum // 2

        s = set()
        s.add(0)

        for num in nums:
            possible_sums = list(s)
            for possible_sum in possible_sums:
                if (possible_sum + num) == target_sum:
                    return True
                s.add(possible_sum + num)

        return target_sum in s

    # use recursion
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)

        if total_sum % 2:
            return False

        dp = [[-1] * (total_sum // 2 + 1) for _ in range(n)]

        def rec(i, target_sum):
            if target_sum == 0:
                return True

            if i == n or target_sum < 0:  # index over n or target_sum < 0
                return False
            elif dp[i][target_sum] != -1:  # use memo
                return dp[i][target_sum]

            # memoize
            dp[i][target_sum] = rec(i + 1, target_sum - nums[i]) or rec(i + 1, target_sum)  # take it or discard
            return dp[i][target_sum]

        return rec(0, total_sum // 2)

    # dp version
    def canPartitionDP(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2:
            return False

        n = len(nums)

        # knapsack problem dp[i][j] =
        # i => level of decision tree
        # j => 0 ~ target sum i.e. total_sum // 2
        dp = [[False] * (total_sum // 2 + 1) for _ in range(n + 1)]
        dp[0][0] = True  # is there a way to take 0 element to have a target sum of 0

        for i in range(1, n + 1):
            for j in range(total_sum // 2 + 1):
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]  # cannot take
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]  # take or not take based on previous level

        return dp[-1][-1]


if __name__ == "__main__":
    assert Solution().canPartition([2, 2, 1, 1])
    assert Solution().canPartition([1, 5, 11, 5])
    assert Solution().canPartition([3, 3, 3, 4, 5])
    assert not Solution().canPartition([1, 1, 1, 1, 1])
    assert not Solution().canPartition([1, 2, 5])
    assert not Solution().canPartition([1, 2, 3, 5])
