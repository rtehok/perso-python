import bisect
from typing import List


class Solution:
    def find132patternTLE(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] < nums[k] < nums[j]:
                        return True

        return False

    def find132patternTLE2(self, nums: List[int]) -> bool:
        min_i = float("inf")
        for j in range(len(nums) - 1):
            min_i = min(min_i, nums[j])
            for k in range(j + 1, len(nums)):
                if min_i < nums[k] < nums[j]:
                    return True

        return False

    def find132patternIntervals(self, nums: List[int]) -> bool:
        intervals = []
        min_point_after_last_peak_index = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if min_point_after_last_peak_index < i - 1:
                    intervals.append(
                        (nums[min_point_after_last_peak_index], nums[i - 1])
                    )  # rising peak
                min_point_after_last_peak_index = i
            for (start, end) in intervals:
                if start < nums[i] < end:
                    return True

        return False

    def find132patternStack(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        stack = []
        min_array = [-1] * n
        min_array[0] = nums[0]
        for i in range(1, n):
            min_array[i] = min(min_array[i - 1], nums[i])

        for j in range(n - 1, -1, -1):
            if nums[j] <= min_array[j]:
                continue
            while stack and stack[-1] <= min_array[j]:
                stack.pop()

            if stack and stack[-1] < nums[j]:
                return True

            stack.append(nums[j])

        return False

    def find132patternBinarySearch(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        min_array = [-1] * n
        min_array[0] = nums[0]
        for i in range(1, n):
            min_array[i] = min(min_array[i - 1], nums[i])

        k = n
        for j in range(n - 1, -1, -1):
            if nums[j] < min_array[j]:
                continue

            k = bisect.bisect_left(nums, min_array[j] + 1, k, n)

            if k < n and nums[k] < nums[j]:
                return True

            k -= 1
            nums[k] = nums[j]

        return False

    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        min_array = [-1] * n
        min_array[0] = nums[0]
        for i in range(1, n):
            min_array[i] = min(min_array[i - 1], nums[i])

        k = n
        for j in range(n - 1, -1, -1):
            if nums[j] < min_array[j]:
                continue

            while k < n and nums[k] <= min_array[j]:
                k += 1

            if k < n and nums[k] < nums[j]:
                return True

            k -= 1
            nums[k] = nums[j]

        return False

if __name__ == "__main__":
    assert not Solution().find132pattern([1, 2, 3, 4])
    assert Solution().find132pattern([3, 1, 4, 2])
    assert Solution().find132pattern([-1, 3, 2, 0])
