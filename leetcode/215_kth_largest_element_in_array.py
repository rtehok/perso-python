import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return sorted(nums)[-k]

        heapq.heapify(nums)

        for i in range(len(nums) - k):
            _ = heapq.heappop(nums)

        return nums[0]


if __name__ == "__main__":
    assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
