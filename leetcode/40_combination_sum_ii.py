from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def helper(nums, current_target, cand):
            if current_target == 0:
                res.append(cand)

            for i in range(len(nums)):
                if nums[i] > current_target:
                    break
                if i > 0 and nums[i - 1] == nums[i]:
                    continue
                helper(nums[i + 1:], current_target - nums[i], cand + [nums[i]])

        helper(candidates, target, [])

        return res


if __name__ == "__main__":
    assert Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    assert Solution().combinationSum2([2, 5, 2, 1, 2], 5) == [[1, 2, 2], [5]]
