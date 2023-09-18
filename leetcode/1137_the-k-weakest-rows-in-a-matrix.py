import heapq
from typing import List


class Solution:
    def kWeakestRowsCount(self, mat: List[List[int]], k: int) -> List[int]:
        rows_with_soldiers = [(i, row.count(1)) for i, row in enumerate(mat)]
        rows_with_soldiers.sort(key=lambda x: (x[1], x[0]))
        return [row[0] for row in rows_with_soldiers[:k]]

    def kWeakestRowsBinarySearch(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat[0])

        def countSoldiers(row):
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid

            return left

        rows_with_soldiers = [(i, countSoldiers(row)) for i, row in enumerate(mat)]
        rows_with_soldiers.sort(key=lambda x: (x[1], x[0]))
        return [row[0] for row in rows_with_soldiers[:k]]

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i, row in enumerate(mat):
            count = sum(row)
            heapq.heappush(heap, (-count, -i))

            if len(heap) > k:
                heapq.heappop(heap)

        return [-item[1] for item in sorted(heap, reverse=True)]


if __name__ == "__main__":
    assert Solution().kWeakestRows(mat=
                                   [[1, 1, 0, 0, 0],
                                    [1, 1, 1, 1, 0],
                                    [1, 0, 0, 0, 0],
                                    [1, 1, 0, 0, 0],
                                    [1, 1, 1, 1, 1]],
                                   k=3) == [2, 0, 3]
    assert Solution().kWeakestRows(mat=
                                   [[1, 0, 0, 0],
                                    [1, 1, 1, 1],
                                    [1, 0, 0, 0],
                                    [1, 0, 0, 0]],
                                   k=2) == [0, 2]
