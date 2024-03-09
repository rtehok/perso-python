from typing import List


class Solution:
    def getCommonTwoPointers(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        if nums1[-1] < nums2[0] or nums1[0] > nums2[-1]:
            return -1

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                return nums1[i]
        return -1

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def search(target, arr):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    return True
            return False

        if len(nums1) > len(nums2):
            self.getCommon(nums2, nums1)

        for num in nums1:
            if search(num, nums2):
                return num

        return -1


assert Solution().getCommon(nums1=[1, 2, 3], nums2=[2, 4]) == 2
assert Solution().getCommon(nums1=[1, 2, 3, 6], nums2=[2, 3, 4, 5]) == 2
