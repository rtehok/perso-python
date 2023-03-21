from typing import List


class Solution:
    def zeroFilledSubarrayV1(self, nums: List[int]) -> int:
        res = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                j = i
                for j in range(i, len(nums) + 1):
                    if j <= len(nums) - 1 and nums[j] != 0:
                        break

                l = len(nums[i:j])

                res += l * (l + 1) // 2
                i = i + l
            else:
                i += 1
        return res

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans, num_sub_array = 0, 0

        for num in nums:
            if num == 0:
                num_sub_array += 1
            else:
                num_sub_array = 0
            ans += num_sub_array

        return ans


if __name__ == "__main__":
    # [0] = 1
    # [0, 0] = [0] * 2 + [0, 0] = 3
    # [0, 0, 0] = [0] * 3 + [0, 0] * 2 + [0, 0, 0] * 1 = 6
    # [0 ,0 ,0 , 0] = [0] * 4 + [0, 0] * 3 + [0, 0, 0] * 2 + [0, 0, 0, 0] * 1 = 10
    # n * (n + 1) // 2 ==> sum of natural numbers (see wikipedia)
    # assert Solution().zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) == 6
    assert Solution().zeroFilledSubarray([0, 0, 0, 2, 0, 0]) == 9
    assert Solution().zeroFilledSubarray([2, 10, 2019]) == 0
