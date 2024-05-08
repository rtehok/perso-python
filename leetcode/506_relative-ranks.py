import collections
import heapq
from typing import List


class Solution:
    def findRelativeRanksHeap(self, score: List[int]) -> List[str]:
        h = []
        for i, s in enumerate(score):
            heapq.heappush(h, (-s, i))

        res = [""] * len(score)

        i = 0
        while h:
            _, idx = heapq.heappop(h)
            if i == 0:
                res[idx] = "Gold Medal"
            elif i == 1:
                res[idx] = "Silver Medal"
            elif i == 2:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(i + 1)

            i += 1

        return res

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        score_to_index = collections.defaultdict(int)

        for i in range(n):
            score_to_index[score[i]] = i

        MEDALS = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        rank = [None] * n

        score.sort(reverse=True)

        for i in range(n):
            if i < 3:
                rank[score_to_index[score[i]]] = MEDALS[i]
            else:
                rank[score_to_index[score[i]]] = str(i + 1)
        return rank


assert Solution().findRelativeRanks([5, 4, 3, 2, 1]) == ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
assert Solution().findRelativeRanks([10, 3, 8, 9, 4]) == ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
