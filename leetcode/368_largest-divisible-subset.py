from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        LIS_len = [1] * n
        prev_idx = [-1] * n
        max_len = 0
        idx = -1

        nums.sort()

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and LIS_len[j] + 1 > LIS_len[i]:
                    LIS_len[i] = 1 + LIS_len[j]
                    prev_idx[i] = j

            if LIS_len[i] > max_len:
                max_len = LIS_len[i]
                idx = i

        ans = set()
        while idx != -1:
            ans.add(nums[idx])
            idx = prev_idx[idx]

        return ans


assert Solution().largestDivisibleSubset([1, 2, 3]) == {1, 2}
assert Solution().largestDivisibleSubset([1, 2, 4, 8]) == {1, 2, 4, 8}
