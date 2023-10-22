import heapq
from typing import List

import sortedcontainers as sortedcontainers


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = k, k
        ans, curr_min = nums[k], nums[k]

        while left > 0 or right < n - 1:
            if left == 0 or (right < n - 1 and nums[right + 1] > nums[left - 1]):
                right += 1
            else:
                left -= 1

            curr_min = min(curr_min, nums[left], nums[right])
            ans = max(ans, curr_min * (right - left + 1))
        return ans


if __name__ == "__main__":
    assert Solution().maximumScore(nums=[1, 4, 3, 7, 4, 5], k=3) == 15
    assert Solution().maximumScore(nums=[5, 5, 4, 5, 4, 1, 1, 1], k=0) == 20
