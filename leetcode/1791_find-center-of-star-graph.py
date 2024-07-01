from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first, second = edges[0], edges[1]

        if first[0] in second:
            return first[0]
        else:
            return first[1]


assert Solution().findCenter(edges=[[1, 2], [2, 3], [4, 2]]) == 2
assert Solution().findCenter(edges=[[1, 2], [5, 1], [1, 3], [1, 4]]) == 1
