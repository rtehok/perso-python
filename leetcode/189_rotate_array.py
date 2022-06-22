from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return

        n = len(nums)
        k = k % n
        nums[k:], nums[:k] = nums[:n - k], nums[n - k:]


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
