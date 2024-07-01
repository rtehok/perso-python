from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 and arr[i + 2] % 2:
                return True

        return False


assert not Solution().threeConsecutiveOdds([2, 6, 4, 1])
assert Solution().threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12])
