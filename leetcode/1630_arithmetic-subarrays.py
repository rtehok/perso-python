from typing import List


class Solution:
    def checkArithmeticSubarraysSortAndCheck(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        n = len(l)

        def isArithmetic(sorted_nums):
            first = sorted_nums[0]
            second = sorted_nums[1] if len(sorted_nums) >= 2 else first
            x = second - first
            for i in range(1, len(sorted_nums) - 1):
                if sorted_nums[i + 1] - sorted_nums[i] != x:
                    return False

            return True

        for i in range(n):
            ans.append(isArithmetic(sorted(nums[l[i]:r[i] + 1])))

        return ans

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # no sort
        def check(arr):
            min_elt = min(arr)
            max_elt = max(arr)
            if (max_elt - min_elt) % (len(arr) - 1) != 0:
                return False

            diff = (max_elt - min_elt) // (len(arr) - 1)
            curr = min_elt + diff
            arr_set = set(arr)
            while curr < max_elt:
                if curr not in arr_set:
                    return False
                curr += diff

            return True

        ans = []
        for i in range(len(l)):
            arr = nums[l[i]: r[i] + 1]
            ans.append(check(arr))

        return ans


if __name__ == "__main__":
    assert Solution().checkArithmeticSubarrays(nums=[-3, -6, -8, -4, -2, -8, -6, 0, 0, 0, 0],
                                               l=[5, 4, 3, 2, 4, 7, 6, 1, 7], r=[6, 5, 6, 3, 7, 10, 7, 4, 10]) == [True,
                                                                                                                   True,
                                                                                                                   True,
                                                                                                                   True,
                                                                                                                   False,
                                                                                                                   True,
                                                                                                                   True,
                                                                                                                   True,
                                                                                                                   True]
    assert Solution().checkArithmeticSubarrays(nums=[4, 6, 5, 9, 3, 7], l=[0, 0, 2], r=[2, 3, 5]) == [True, False, True]
    assert Solution().checkArithmeticSubarrays(nums=[-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
                                               l=[0, 1, 6, 4, 8, 7], r=[4, 4, 9, 7, 9, 10]) == [False, True, False,
                                                                                                False, True, True]
