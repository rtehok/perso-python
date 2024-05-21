from typing import List


class Solution:
    def subsetsBacktrack(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx, curr):
            ans.append(curr[:])
            for j in range(idx, len(nums)):
                curr.append(nums[j])
                dfs(j + 1, curr)
                curr.pop()

        ans = []
        dfs(0, [])
        return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for num in nums:
            ans += [curr + [num] for curr in ans]

        return ans


assert Solution().subsets([1, 2, 3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
assert Solution().subsets(nums=[0]) == [[], [0]]
