from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        return [list(nums1 - nums2), list(nums2 - nums1)]


if __name__ == "__main__":
    assert Solution().findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]) == [[1, 3], [4, 6]]
    assert Solution().findDifference(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]) == [[3], []]
