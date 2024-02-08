import collections
from typing import List


class Solution:
    def groupThePeopleV1(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        groups = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            if size in groups and len(groups[size][-1]) < size:
                groups[size][-1].append(i)
            else:
                groups[size].append([i])
        for k, v_arr in groups.items():
            for v in v_arr:
                ans.append(v)

        return ans

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        groups = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                ans.append(groups.pop(size))

        return ans


if __name__ == "__main__":
    sol = Solution().groupThePeople(groupSizes=[3, 3, 3, 3, 3, 1, 3])
    assert [5] in sol
    assert [0, 1, 2] in sol
    assert [3, 4, 6] in sol

    sol = Solution().groupThePeople(groupSizes=[2, 1, 3, 3, 3, 2])
    assert [1] in sol
    assert [0, 5] in sol
    assert [2, 3, 4] in sol
