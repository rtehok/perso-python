from typing import List


class Solution:
    def shuffleExtraArray(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n + i])

        return res

    def shuffleGenerator(self, nums: List[int], n: int) -> List[int]:
        return [nums[j] for i in range(n) for j in range(i, i + n + 1, n)]

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n, 2 * n):
            second_num = nums[i] << 10  # shift y to left
            nums[i - n] |= second_num  # store it next to x

        # '0000000000 1111111111' in decimal.
        all_ones = int(pow(2, 10)) - 1  # 1023

        for i in range(n - 1, -1, -1):
            second_num = nums[i] >> 10  # extract y
            first_num = nums[i] & all_ones  # extract x
            nums[2 * i + 1] = second_num
            nums[2 * i] = first_num

        return nums


if __name__ == "__main__":
    assert Solution().shuffle(nums=[2, 5, 1, 3, 4, 7], n=3) == [2, 3, 5, 4, 1, 7]
    assert Solution().shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4) == [1, 4, 2, 3, 3, 2, 4, 1]
    assert Solution().shuffle(nums=[1, 1, 2, 2], n=2) == [1, 2, 1, 2]
