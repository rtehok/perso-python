import collections
from typing import List


class Solution:
    def findDiagonalOrderTLE(self, nums: List[List[int]]) -> List[int]:
        if len(nums) == 1:
            return nums[0]

        max_len = max(len(row) for row in nums)
        tx = 0
        res = []

        while tx < len(nums):
            dx, dy = tx, 0
            while 0 <= dx and dy < max_len:
                if dy < len(nums[dx]):
                    res.append(nums[dx][dy])
                dx -= 1
                dy += 1
            tx += 1

        ty = 1

        while ty < max_len:
            dx, dy = len(nums) - 1, ty
            while dy < max_len:
                if 0 <= dx and dy < len(nums[dx]):
                    res.append(nums[dx][dy])
                dx -= 1
                dy += 1
            ty += 1

        return res

    def findDiagonalOrderV1(self, nums: List[List[int]]) -> List[int]:
        groups = collections.defaultdict(list)
        for r in range(len(nums) - 1, -1, -1):
            for c in range(len(nums[r])):
                diagonal = r + c
                groups[diagonal].append(nums[r][c])

        ans = []
        curr = 0
        while curr in groups:
            ans.extend(groups[curr])
            curr += 1

        return ans

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        q = collections.deque([(0, 0)])
        ans = []

        while q:
            r, c = q.popleft()
            ans.append(nums[r][c])

            if c == 0 and r + 1 < len(nums):  # add below if first column
                q.append((r + 1, c))

            if c + 1 < len(nums[r]):  # add right
                q.append((r, c + 1))

        return ans


if __name__ == "__main__":
    assert Solution().findDiagonalOrder([
        [3, 3, 18],
        [4, 15, 11],
        [19, 11, 14, 14, 3]
    ]) == [3, 4, 3, 19, 15, 18, 11, 11, 14, 14, 3]
    assert Solution().findDiagonalOrder([[1, 2, 3, 4, 5, 6]]) == [1, 2, 3, 4, 5, 6]
    assert Solution().findDiagonalOrder(nums=[[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]) == \
           [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16]
    assert Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 4, 2, 7, 5, 3, 8, 6, 9]
