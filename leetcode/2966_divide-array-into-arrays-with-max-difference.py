from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(1, n - 1, 3):
            if nums[i] - nums[i - 1] <= k and nums[i + 1] - nums[i] <= k and nums[i + 1] - nums[i - 1] <= k:
                ans.append([nums[i - 1], nums[i], nums[i + 1]])
            else:
                return []
        return ans


assert Solution().divideArray(nums=[1, 3, 4, 8, 7, 9, 3, 5, 1], k=2) == [[1, 1, 3], [3, 4, 5], [7, 8, 9]]
assert Solution().divideArray(nums=[1, 3, 3, 2, 7, 3], k=3) == []
