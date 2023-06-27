import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        res = []

        visited = set()

        min_heap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))

        while k > 0 and min_heap:
            val, (i, j) = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])

            if i + 1 < m and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], (i + 1, j)))

            if j + 1 < n and (i, j + 1) not in visited:
                visited.add((i, j + 1))
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], (i, j + 1)))

            k -= 1

        return res


if __name__ == "__main__":
    assert Solution().kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3) == [[1, 2], [1, 4], [1, 6]]
    assert Solution().kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2) == [[1, 1], [1, 1]]
    assert Solution().kSmallestPairs(nums1=[1, 2], nums2=[3], k=3) == [[1, 3], [2, 3]]
