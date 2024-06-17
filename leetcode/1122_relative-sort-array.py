from typing import List
import collections


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = collections.Counter(arr1)
        ans = []
        for num in arr2:
            for _ in range(cnt[num]):
                ans.append(num)
            cnt.pop(num)

        remaining = []
        for k, v in cnt.items():
            remaining.extend([k] * v)

        return ans + sorted(remaining)


assert Solution().relativeSortArray(arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]) == [2, 2, 2, 1, 4,
                                                                                                          3, 3, 9, 6, 7,
                                                                                                          19]
assert Solution().relativeSortArray(arr1=[28, 6, 22, 8, 44, 17], arr2=[22, 28, 8, 6]) == [22, 28, 8, 6, 17, 44]
