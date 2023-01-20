from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> set[tuple[int]]:
        res = set()
        sequence = []

        def backtrack(index):
            if index == len(nums):
                if len(sequence) >= 2:
                    res.add(tuple(sequence))
                return

            if not sequence or sequence[-1] <= nums[index]:
                sequence.append(nums[index])
                backtrack(index + 1)
                sequence.pop()

            backtrack(index + 1)

        backtrack(0)
        return res


if __name__ == "__main__":
    assert Solution().findSubsequences([4, 6, 7, 7]) == {(4, 6), (4, 6, 7), (4, 6, 7, 7), (4, 7), (4, 7, 7), (6, 7),
                                                         (6, 7, 7), (7, 7)}
    assert Solution().findSubsequences([4, 4, 3, 2, 1]) == {(4, 4)}
