from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        stack = [(0, 0, [])]

        while stack:
            current_sum, idx, cand = stack.pop()
            if current_sum == target:
                res.append(cand)
            for i in range(idx, len(candidates)):
                if current_sum + candidates[i] <= target:
                    stack.append([current_sum + candidates[i], i, cand + [candidates[i]]])
        return res


if __name__ == "__main__":
    assert Solution().combinationSum([2, 3, 6, 7], 7) == [[7], [2, 2, 3]]
    assert Solution().combinationSum([2, 3, 5], 8) == [[3, 5], [2, 3, 3], [2, 2, 2, 2]]
    assert Solution().combinationSum([2], 1) == []
