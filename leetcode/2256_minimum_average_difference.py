import math
from typing import List


class Solution:
    # O(n2)
    def minimumAverageDifferenceBruteForce(self, nums: List[int]) -> int:
        min_res = math.inf
        min_index = 0

        for i, n in enumerate(nums):
            s = sum(nums[:i + 1])
            right = sum(nums[i + 1:]) // len(nums[i + 1:]) if i < len(nums) - 1 else 0
            tmp = abs(s // (i + 1) - right)
            if tmp < min_res:
                min_res = tmp
                min_index = i

        return min_index

    # prefix sum => TC O(n) / SC O(n)
    def minimumAverageDifferencePrefix(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)

        min_res = math.inf
        min_index = -1

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]

        for i in range(n):
            left_avg = prefix[i + 1]
            left_avg //= (i + 1)

            right_avg = suffix[i + 1]
            if i != n - 1:
                right_avg //= n - i - 1

            tmp = abs(left_avg - right_avg)

            if tmp < min_res:
                min_res = tmp
                min_index = i

        return min_index

    # prefix sum / space optimized => TC O(n) / SC O(1)
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        min_index = -1
        min_res = math.inf
        total_sum = sum(nums)

        curr_prefix_sum = 0

        for i in range(n):
            curr_prefix_sum += nums[i]
            left_avg = curr_prefix_sum
            left_avg //= i + 1

            right_avg = total_sum - curr_prefix_sum
            if i != n - 1:
                right_avg //= n - i - 1

            tmp = abs(left_avg - right_avg)

            if tmp < min_res:
                min_res = tmp
                min_index = i

        return min_index


if __name__ == "__main__":
    assert Solution().minimumAverageDifference([2, 5, 3, 9, 5, 3]) == 3
    assert Solution().minimumAverageDifference([0]) == 0
    assert Solution().minimumAverageDifference([0, 0, 0, 0, 0]) == 0
