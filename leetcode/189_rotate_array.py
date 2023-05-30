from typing import List


class Solution:
    def rotateV1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return

        n = len(nums)
        k = k % n
        nums[k:], nums[:k] = nums[:n - k], nums[n - k:]

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return

        n = len(nums)
        k %= n  # handle k > n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # 1 2 3 4 5 6 7
        reverse(0, n - 1)  # 7 6 5 4 3 2 1
        reverse(0, k - 1)  # 5 6 7 - - - -
        reverse(k, n - 1)  # - - - 1 2 3 4


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(a, 3)
    assert a == [5, 6, 7, 1, 2, 3, 4]

    a = [-1, -100, 3, 99]
    Solution().rotate(a, 2)
    assert a == [3, 99, -1, -100]

    a = [1, 2]
    Solution().rotate(a, 0)
    assert a == [1, 2]

    a = [1, 2]
    Solution().rotate(a, 2)
    assert a == [1, 2]
