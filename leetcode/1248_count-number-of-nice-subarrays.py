from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        curr_sum = 0
        prefix_sum = {curr_sum: 1}

        subarrays = 0

        for i in range(n):
            curr_sum += nums[i] % 2
            if curr_sum - k in prefix_sum:
                subarrays += prefix_sum[curr_sum - k]
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

        return subarrays


assert Solution().numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3) == 2
assert Solution().numberOfSubarrays(nums=[2, 4, 6], k=1) == 0
assert Solution().numberOfSubarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2) == 16
