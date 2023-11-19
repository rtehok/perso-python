from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        up = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                up += 1

            ans += up

        return ans


if __name__ == "__main__":
    assert Solution().reductionOperations(nums=[5, 1, 3]) == 3
    assert Solution().reductionOperations(nums=[1, 1, 1]) == 0
    assert Solution().reductionOperations(nums=[1, 1, 2, 2, 3]) == 4
