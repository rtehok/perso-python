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


if __name__ == "__main__":
    assert Solution().rob([2, 7, 9, 3, 1]) == 12
    assert Solution().rob([2, 1, 1, 2]) == 4
