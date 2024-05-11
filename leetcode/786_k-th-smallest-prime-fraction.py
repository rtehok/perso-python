import heapq
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        pq = []

        for i in range(len(arr)):
            heapq.heappush(pq, ((arr[i] / arr[-1]), i, len(arr) - 1))

        for _ in range(k - 1):
            _, numerator_idx, denominator_idx = heapq.heappop(pq)
            denominator_idx -= 1
            if denominator_idx > numerator_idx:
                heapq.heappush(pq, ((arr[numerator_idx] / arr[denominator_idx]), numerator_idx, denominator_idx))

        _, numerator_idx, denominator_idx = heapq.heappop(pq)
        return [arr[numerator_idx], arr[denominator_idx]]


assert Solution().kthSmallestPrimeFraction([1, 2, 3, 5], 3) == [2, 5]
assert Solution().kthSmallestPrimeFraction([1, 7], 1) == [1, 7]
