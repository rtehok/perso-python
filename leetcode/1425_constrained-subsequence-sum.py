import heapq
from typing import List

import sortedcontainers as sortedcontainers


class Solution:
    def constrainedSubsetSumHeap(self, nums: List[int], k: int) -> int:
        heap = [(-nums[0], 0)]
        ans = nums[0]

        for i in range(1, len(nums)):
            while i - heap[0][1] > k:
                heapq.heappop(heap)

            curr = max(0, -heap[0][0]) + nums[i]
            ans = max(ans, curr)
            heapq.heappush(heap, (-curr, i))

        return ans

    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        window = sortedcontainers.SortedList([0])
        dp = [0] * len(nums)

        for i in range(len(nums)):
            dp[i] = nums[i] + window[-1]
            window.add(dp[i])
            if i >= k:
                window.remove(dp[i - k])

        return max(dp)


if __name__ == "__main__":
    assert Solution().constrainedSubsetSum(nums=[10, 2, -10, 5, 20], k=2) == 37
    assert Solution().constrainedSubsetSum(nums=[-1, -2, -3], k=1) == -1
    assert Solution().constrainedSubsetSum(nums=[10, -2, -10, -5, 20], k=2) == 23
