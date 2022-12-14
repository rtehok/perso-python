from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        #
        # if len(nums) == 2:
        #     return max(nums[0], nums[1])
        #
        # res = [nums[0], max(nums[0], nums[1])]
        # for i in range(2, len(nums)):
        #     res.append(max(res[i - 2] + nums[i], res[i - 1]))
        #
        # return res[-1]

        m1 = 0  # house - 1
        m2 = 0  # house - 2

        for rob in nums:
            tmp = m1
            m1 = max(m1, m2 + rob)
            m2 = tmp

        return m1

    def rob_mutate(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        for i in range(2, n):
            nums[i] = max(nums[i - 1], nums[i - 2] + nums[i])
            nums[i - 1] = max(nums[i - 1], nums[i - 2])

        return nums[-1]

    def rob_sub_optimal(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        h_1 = nums[1]  # house - 1
        h_2 = nums[0]  # house - 2

        for i in range(2, n):
            curr = max(h_1, h_2 + nums[i])
            h_2 = max(h_1, h_2)
            h_1 = curr

        return curr


if __name__ == "__main__":
    assert Solution().rob([2, 7, 9, 3, 1]) == 12
    assert Solution().rob([2, 1, 1, 2]) == 4
