from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i = j = 0

        res = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1

        return res


assert Solution().intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]) == [2, 2]
assert Solution().intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]) == [4, 9]
