import heapq
import math
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        h = []
        min_value = math.inf

        for num in nums:
            if num % 2 == 1:
                min_value = min(min_value, num * 2)
                heapq.heappush(h, -num * 2)
            else:
                min_value = min(min_value, num)
                heapq.heappush(h, -num)

        min_deviation = math.inf

        while True:
            max_value = -heapq.heappop(h)
            min_deviation = min(min_deviation, max_value - min_value)
            if max_value % 2 == 1:
                break
            max_value //= 2
            min_value = min(min_value, max_value)
            heapq.heappush(h, -max_value)

        return min_deviation


if __name__ == "__main__":
    assert Solution().minimumDeviation(nums=[1, 2, 3, 4]) == 1
    assert Solution().minimumDeviation(nums=[4, 1, 5, 20, 3]) == 3
