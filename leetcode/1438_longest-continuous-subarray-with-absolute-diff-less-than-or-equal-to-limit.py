import heapq
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        max_heap = []
        min_heap = []
        left = 0
        max_length = 0

        for right in range(n):
            heapq.heappush(max_heap, (-nums[right], right))
            heapq.heappush(min_heap, (nums[right], right))

            while -max_heap[0][0] - min_heap[0][0] > limit:
                left = min(max_heap[0][1], min_heap[0][1]) + 1

                while max_heap[0][1] < left:
                    heapq.heappop(max_heap)

                while min_heap[0][1] < left:
                    heapq.heappop(min_heap)

            max_length = max(max_length, right - left + 1)

        return max_length


assert Solution().longestSubarray(nums=[8, 2, 4, 7], limit=4) == 2
assert Solution().longestSubarray(nums=[10, 1, 2, 4, 7, 2], limit=5) == 4
assert Solution().longestSubarray(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0) == 3
