import bisect
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted([s for s, _ in flowers])
        ends = sorted([e for _, e in flowers])
        return [bisect.bisect_right(starts, t) - bisect.bisect_left(ends, t) for t in people]  # t = time_person_arrives


if __name__ == "__main__":
    assert Solution().fullBloomFlowers(flowers=[[1, 6], [3, 7], [9, 12], [4, 13]], people=[2, 3, 7, 11]) == [1, 2, 2, 2]
    assert Solution().fullBloomFlowers(flowers=[[1, 10], [3, 3]], people=[3, 3, 2]) == [2, 2, 1]
