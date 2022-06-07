from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        for x in range(m + n - 1, -1, -1):
            if j < 0:
                return

            if i >= 0 and nums1[i] > nums2[j]:
                nums1[x] = nums1[i]
                i -= 1
            else:
                nums1[x] = nums2[j]
                j -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    Solution().merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]
    nums1 = [1]
    Solution().merge([1], 1, [], 0)
    assert nums1 == [1]
    nums1 = [0]
    Solution().merge([0], 0, [1], 1)
    assert nums1 == [1]

