from typing import List


class Solution:
    def intersectionV1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

    def intersectionTwoPointers(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        first, second = 0, 0
        m, n = len(nums1), len(nums2)
        ans = set()

        while first < m and second < n:
            if nums1[first] == nums2[second]:
                ans.add(nums1[first])
                first += 1
                second += 1
            elif nums1[first] < nums2[second]:
                first += 1
            else:
                second += 1
        return list(ans)

    def intersectionDict(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        res = []

        for x in nums1:
            seen.add(x)

        for x in nums2:
            if x in seen:
                res.append(x)
                seen.remove(x)

        return res

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def set_intersection(set1, set2):
            return [x for x in set1 if x in set2]

        s1, s2 = set(nums1), set(nums2)
        if len(s1) < len(s2):
            return set_intersection(s1, s2)
        else:
            return set_intersection(s2, s1)


assert Solution().intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]) == [2]
assert Solution().intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]) == [9, 4]
