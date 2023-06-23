from typing import List


class Solution:
    # TC O(n3)
    def longestArithSeqLengthBruteForce(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return n

        longest = 2

        for i in range(n):
            for j in range(i + 1, n):
                diff = nums[j] - nums[i]
                cnt = 2
                prev = nums[j]

                for k in range(j + 1, n):
                    if nums[k] - prev == diff:
                        cnt += 1
                        prev = nums[k]
                longest = max(longest, cnt)

        return longest

    # TC O(n2) / SC O(n2)
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)

        # let dp[right][diff] represent the length of the longest arithmetic sequence that ends with the element at index right
        # and has a common difference of diff
        # dp[right][diff] = dp[left][diff] + 1
        dp = {}

        for right in range(n):
            for left in range(0, right):
                dp[(right, nums[right] - nums[left])] = dp.get((left, nums[right] - nums[left]), 1) + 1

        return max(dp.values())


if __name__ == "__main__":
    assert Solution().longestArithSeqLength([3, 6, 9, 12]) == 4
    assert Solution().longestArithSeqLength([9, 4, 7, 2, 10]) == 3
    assert Solution().longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]) == 4
