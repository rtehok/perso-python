from typing import List


class SolutionV1:
    def dfs(self, nums: List[int], path: List[int], res: List[List[int]], k: int) -> None:
        if len(path) == k:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i + 1:], path + [nums[i]], res, k)

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        arr = [i for i in range(1, n + 1)]
        self.dfs(arr, [], res, k)

        return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])

            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])

        return res


if __name__ == "__main__":
    assert Solution().combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert Solution().combine(1, 1) == [[1]]
