from bisect import bisect_left, bisect_right
from typing import List
import collections


class Solution:
    def findSpecialIntegerV1(self, arr: List[int]) -> int:
        cnt = collections.Counter(arr)
        n = len(arr)
        target = n / 4
        for k, v in cnt.items():
            if v > target:
                return k
        return 0

    def findSpecialIntegerV2(self, arr: List[int]) -> int:
        cnt = collections.defaultdict(int)
        n = len(arr)
        target = n / 4
        for v in arr:
            cnt[v] += 1
            if cnt[v] > target:
                return v
        return 0

    def findSpecialIntegerV3(self, arr: List[int]) -> int:
        size = len(arr) // 4
        for i in range(len(arr) - size):
            if arr[i] == arr[i + size]:
                return arr[i]

        return -1

    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        candidates = [arr[n // 4], arr[n // 2], arr[3 * n // 4]]
        target = n / 4
        for candidate in candidates:
            left = bisect_left(arr, candidate)
            right = bisect_right(arr, candidate) - 1
            if right - left + 1 > target:
                return candidate
        return -1


if __name__ == "__main__":
    assert Solution().findSpecialInteger(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]) == 6
    assert Solution().findSpecialInteger(arr=[1, 1]) == 1
