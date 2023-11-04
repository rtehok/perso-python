from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans = 0
        for num in left:
            ans = max(ans, num)

        for num in right:
            ans = max(ans, n - num)

        return ans


if __name__ == "__main__":
    assert Solution().getLastMoment(n=4, left=[4, 3], right=[0, 1]) == 4
    assert Solution().getLastMoment(n=7, left=[], right=[0, 1, 2, 3, 4, 5, 6, 7]) == 7
    assert Solution().getLastMoment(n=7, left=[0, 1, 2, 3, 4, 5, 6, 7], right=[]) == 7
