from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) > 1:
            if stones[0] == stones[1]:
                stones = stones[2:]
                stones.append(0)
            else:
                diff = stones[0] - stones[1]
                stones = stones[2:]
                stones.append(diff)
                stones.sort(reverse=True)

        return stones[0]


if __name__ == "__main__":
    assert Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert Solution().lastStoneWeight([1]) == 1
    assert Solution().lastStoneWeight([2, 2]) == 0
