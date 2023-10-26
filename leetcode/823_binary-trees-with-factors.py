from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        arr.sort()
        dp = [1] * len(arr)
        index = {v: i for i, v in enumerate(arr)}

        for i, node_value in enumerate(arr):
            for j in range(i):
                if node_value % arr[j] == 0:  # arr[j] is the left node
                    right_node = node_value / arr[j]
                    if right_node in index:
                        dp[i] += dp[j] * dp[index[right_node]]
                        dp[i] %= MOD

        return sum(dp) % MOD


if __name__ == "__main__":
    assert Solution().numFactoredBinaryTrees([2, 4]) == 3
    assert Solution().numFactoredBinaryTrees([2, 4, 5, 10]) == 7
    assert Solution().numFactoredBinaryTrees([18, 3, 6, 2]) == 12
