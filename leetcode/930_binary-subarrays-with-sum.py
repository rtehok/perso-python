from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total_count = 0
        current_sum = 0
        freq = {}

        for num in nums:
            current_sum += num
            if current_sum == goal:
                total_count += 1

            if current_sum - goal in freq:
                total_count += freq[current_sum - goal]

            freq[current_sum] = freq.get(current_sum, 0) + 1

        return total_count


assert Solution().numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2) == 4
assert Solution().numSubarraysWithSum(nums=[0, 0, 0, 0, 0], goal=0) == 15
