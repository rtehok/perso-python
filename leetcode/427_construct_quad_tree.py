from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        def sameValue(x, y, length):
            for i in range(x, x + length):
                for j in range(y, y + length):
                    if grid[i][j] != grid[x][y]:
                        return False
            return True

        def solve(x, y, length):
            if sameValue(x, y, length):  # is a leaf
                return Node(grid[x][y] == 1, 1, None, None, None, None)
            root = Node(1, 0, None, None, None, None)
            L = length // 2
            root.topLeft = solve(x, y, L)
            root.topRight = solve(x, y + L, L)
            root.bottomLeft = solve(x + L, y, L)
            root.bottomRight = solve(x + L, y + L, L)

            return root

        s = solve(0, 0, len(grid))
        return s


if __name__ == "__main__":
    Solution().construct([[0, 1], [1, 0]])
    # == Node(1, 0,
    #       Node(0, 1, None, None, None, None),
    #       Node(1, 1, None, None, None, None),
    #       Node(1, 1, None, None, None, None),
    #       Node(0, 1, None, None, None, None)
    #       )
    Solution().construct([[1, 1, 1, 1, 0, 0, 0, 0],
                          [1, 1, 1, 1, 0, 0, 0, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 0, 0, 0, 0],
                          [1, 1, 1, 1, 0, 0, 0, 0],
                          [1, 1, 1, 1, 0, 0, 0, 0],
                          [1, 1, 1, 1, 0, 0, 0, 0]])
    # == Node(1, 0,
    #         Node(1, 1, None, None, None, None),
    #         Node(1, 0,
    #              Node(0, 1, None, None, None, None),
    #              Node(0, 1, None, None, None, None),
    #              Node(1, 1, None, None, None, None),
    #              Node(1, 1, None, None, None, None)
    #              ),
    #         Node(1, 1, None, None, None, None),
    #         Node(0, 1, None, None, None, None)
    #         )
