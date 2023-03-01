from typing import List


class Solution:
    def sortArrayMergeSort(self, nums: List[int]) -> List[int]:
        tmp = [0] * len(nums)

        def merge(left, mid, right):
            # calculate starts and sizes of 2 halves
            start1 = left
            start2 = mid + 1
            n1 = mid - left + 1
            n2 = right - mid

            # copy to tmp
            for i in range(n1):
                tmp[start1 + i] = nums[start1 + i]
            for i in range(n2):
                tmp[start2 + i] = nums[start2 + i]

            # Merge the sub-arrays 'in tmp' back into the original array 'arr' in sorted order.
            i, j, k, = 0, 0, left
            while i < n1 and j < n2:
                if tmp[start1 + i] <= tmp[start2 + j]:
                    nums[k] = tmp[start1 + i]
                    i += 1
                else:
                    nums[k] = tmp[start2 + j]
                    j += 1
                k += 1

            # Copy remaining elements
            while i < n1:
                nums[k] = tmp[start1 + i]
                i += 1
                k += 1
            while j < n2:
                nums[k] = tmp[start2 + j]
                j += 1
                k += 1

        # recursive function to split and merge
        def mergeSort(left, right):
            if left >= right:
                return
            mid = (left + right) // 2
            mergeSort(left, mid)
            mergeSort(mid + 1, right)
            merge(left, mid, right)

        mergeSort(0, len(nums) - 1)
        return nums

    # Merge sort / short version
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) == 1:
                return arr

            mid = len(arr) // 2
            l = mergeSort(arr[:mid])
            r = mergeSort(arr[mid:])
            i, j = 0, 0
            res = []
            while i < len(l) or j < len(r):
                if (i < len(l) and j >= len(r)) or (i < len(l) and j < len(r) and l[i] <= r[j]):
                    res.append(l[i])
                    i += 1
                else:
                    res.append(r[j])
                    j += 1
            return res

        return mergeSort(nums)


if __name__ == "__main__":
    assert Solution().sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
    assert Solution().sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5]
