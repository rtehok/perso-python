from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_elt = max(nums)
        ans = start = max_elt_in_window = 0
        for end in range(len(nums)):
            if nums[end] == max_elt:
                max_elt_in_window += 1
            while max_elt_in_window == k:
                if nums[start] == max_elt:
                    max_elt_in_window -= 1
                start += 1
            ans += start
        return ans


assert Solution().countSubarrays(nums=[1, 3, 2, 3, 3], k=2) == 6
assert Solution().countSubarrays(nums=[1, 4, 2, 1], k=3) == 0
