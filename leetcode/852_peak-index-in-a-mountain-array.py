from typing import List


class Solution:
    def peakIndexInMountainArrayLinear(self, arr: List[int]) -> int:
        i = 0
        while arr[i] < arr[i + 1]:
            i += 1
        return i

    def peakIndexInMountainArrayV1(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = right - (right - left) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                right = mid
            else:
                return mid

        return left

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    assert Solution().peakIndexInMountainArray([0, 1, 0]) == 1
    assert Solution().peakIndexInMountainArray([0, 2, 1, 0]) == 1
    assert Solution().peakIndexInMountainArray([0, 10, 5, 2]) == 1
