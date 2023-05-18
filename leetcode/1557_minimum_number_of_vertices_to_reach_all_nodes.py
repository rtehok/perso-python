from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        is_incoming_edge_exists = [False] * n
        for a, b in edges:
            is_incoming_edge_exists[b] = True

        res = []

        for i in range(n):
            if not is_incoming_edge_exists[i]:
                res.append(i)

        return res


if __name__ == "__main__":
    assert Solution().findSmallestSetOfVertices(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]) == [0, 3]
    assert Solution().findSmallestSetOfVertices(n=5, edges=[[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]) == [0, 2, 3]
    assert Solution().findSmallestSetOfVertices(n=3, edges=[[1, 2], [1, 0], [0, 2]]) == [1]
