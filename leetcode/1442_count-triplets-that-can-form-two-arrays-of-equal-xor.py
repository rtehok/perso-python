from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            a = arr[i]
            for j in range(i + 1, n):
                a ^= arr[j]
                b = arr[j]
                for k in range(j, n):
                    b ^= arr[k]
                    if a == b:
                        ans += 1

        return ans


assert Solution().countTriplets([2, 3, 1, 6, 7]) == 4
assert Solution().countTriplets([1, 1, 1, 1, 1]) == 10
