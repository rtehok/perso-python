from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        #
        # nums.sort()
        #
        # c = 1
        # res = 1
        #
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i - 1]:
        #         if nums[i] == nums[i - 1] + 1:
        #             c += 1
        #         else:
        #             res = max(res, c)
        #             c = 1
        #
        # return max(c, res)

        if not nums:
            return 0

        num_set = set(nums)

        res = 1

        for num in nums:
            if not num - 1 in num_set:  # reset
                c = 1

                while num + 1 in num_set:
                    c += 1
                    num += 1

                res = max(res, c)

        return res


if __name__ == "__main__":
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
