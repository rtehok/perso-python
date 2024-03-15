from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1

        for num in nums:
            total *= num

        ans = []

        for i, num in enumerate(nums):
            if num != 0:
                ans.append(total // num)
            else:
                tmp = 1
                for left in nums[:i]:
                    tmp *= left
                for right in nums[i + 1:]:
                    tmp *= right
                ans.append(tmp)

        return ans

    def productExceptSelfV1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        l = r = 1
        for i in range(1, n):
            l *= nums[i - 1]
            res[i] *= l

        for i in range(n - 2, -1, -1):
            r *= nums[i + 1]
            res[i] *= r

        return res


assert Solution().productExceptSelf(nums=[1, 2, 3, 4]) == [24, 12, 8, 6]
assert Solution().productExceptSelf(nums=[-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
