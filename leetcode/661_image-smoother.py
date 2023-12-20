import math
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]

        def calculate_smooth(x, y):
            ans = 0
            nb = 0
            for dx, dy in [(0, 0), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    ans += img[nx][ny]
                    nb += 1
            return math.floor(ans / nb)

        for i in range(m):
            for j in range(n):
                res[i][j] = calculate_smooth(i, j)

        return res


assert Solution().imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]) == [[137, 141, 137],
                                                                                        [141, 138, 141],
                                                                                        [137, 141, 137]]
assert Solution().imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
