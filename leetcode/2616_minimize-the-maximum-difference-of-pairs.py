from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)

        def countValidPairs(threshold):
            index, count = 0, 0
            while index < n - 1:
                if nums[index + 1] - nums[index] <= threshold:
                    count += 1
                    index += 1
                index += 1
            return count

        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if countValidPairs(mid) >= p:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    assert Solution().minimizeMax(nums=[10, 1, 2, 7, 1, 3], p=2) == 1
    assert Solution().minimizeMax(nums=[4, 2, 1, 2], p=1) == 0
