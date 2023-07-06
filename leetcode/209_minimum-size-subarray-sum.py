from typing import List


class Solution:
    # TC O(n)
    def minSubArrayLenV1(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        min_len = float("inf")
        cur_sum = 0
        for right in range(n):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1

        return 0 if min_len == float("inf") else min_len

    # TC O(n * log(n))
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(num + prefix_sum[-1])

        min_len = float("inf")

        for i in range(n):
            left = i + 1
            right = n

            while left <= right:
                mid = right - (right - left) // 2
                sum_range = prefix_sum[mid] - prefix_sum[i]
                if sum_range >= target:
                    min_len = min(min_len, mid - i)
                    right = mid - 1
                else:
                    left = mid + 1

        return 0 if min_len == float("inf") else min_len


if __name__ == "__main__":
    assert Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]) == 2
    assert Solution().minSubArrayLen(target=4, nums=[1, 4, 4]) == 1
    assert Solution().minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]) == 0
