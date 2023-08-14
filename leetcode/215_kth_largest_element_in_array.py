import heapq
from random import random
from typing import List


class Solution:
    def findKthLargestV1(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

    def findKthLargestHeap(self, nums: List[int], k: int) -> int:
        arr = []
        for num in nums:
            heapq.heappush(arr, num)
            if len(arr) > k:
                heapq.heappop(arr)

        return arr[0]

    def findKthLargestQuickSelect(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num == pivot:
                    mid.append(num)
                elif num > pivot:
                    left.append(num)
                else:
                    right.append(num)

            if len(left) >= k:
                return quickSelect(left, k)

            if len(left) + len(mid) < k:
                return quickSelect(right, k - len(left) - len(mid))

            return pivot

        return quickSelect(nums, k)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        max_val = max(nums)
        count = [0] * (max_val - min_val + 1)

        for num in nums:
            count[num - min_val] += 1

        remain = k
        for num in range(len(count) - 1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + min_val

        return -1


if __name__ == "__main__":
    assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
