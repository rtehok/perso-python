from typing import List


class Solution:
    def maxFrequencyV1(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        ans = 0
        curr = 0
        for right in range(len(nums)):
            target = nums[right]
            curr += target

            while (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1

            ans = max(ans, right - left + 1)

        return ans

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        curr = 0

        for right in range(len(nums)):
            target = nums[right]
            curr += target

            if (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1

        return len(nums) - left


if __name__ == "__main__":
    assert Solution().maxFrequency(nums=[1, 2, 4], k=5) == 3
    assert Solution().maxFrequency(nums=[1, 4, 8, 13], k=5) == 2
    assert Solution().maxFrequency(nums=[3, 9, 6], k=2) == 1
