from typing import List


class Solution:
    def sortArrayByParityV1(self, nums: List[int]) -> List[int]:
        odd, even = [], []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        return even + odd

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] % 2 == 0:
                i += 1
            while i < j and nums[j] % 2 == 1:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        return nums


if __name__ == "__main__":
    assert Solution().sortArrayByParity([3, 1, 2, 4]) in ([2, 4, 3, 1], [4, 2, 1, 3])
    assert Solution().sortArrayByParity([0]) == [0]
