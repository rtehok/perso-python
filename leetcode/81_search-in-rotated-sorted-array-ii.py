from typing import List


class Solution:
    def searchV1(self, nums: List[int], target: int) -> bool:
        return target in set(nums)

    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 0:
            return False

        start, end = 0, n - 1

        def existInFirst(start, elt):
            return nums[start] <= elt

        def isBinarySearchHelpful(left, elt):
            return nums[left] != elt

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True

            if not isBinarySearchHelpful(start, nums[mid]):
                start += 1
                continue

            pivot_array = existInFirst(start, nums[mid])
            target_array = existInFirst(start, target)

            if pivot_array ^ target_array:
                if pivot_array:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

        return False


if __name__ == "__main__":
    assert Solution().search([1, 0, 1, 1, 1], 0)
    assert Solution().search(nums=[2, 5, 6, 0, 0, 1, 2], target=0)
    assert not Solution().search(nums=[2, 5, 6, 0, 0, 1, 2], target=3)
