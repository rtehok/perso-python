import collections
from typing import List


class Solution:
    def groupThePeopleV1(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        d = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            if size == 1:
                res.append([i])
                continue

            if len(d[size]) < size:
                d[size].append(i)
            elif len(d[size]) == size:
                res.append(d[size])
                d[size] = [i]

        for size, arr in d.items():
            if size == len(arr):
                res.append(d[size])

        return res

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        groups = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                res.append(groups.pop(size))

        return res


if __name__ == "__main__":
    sol = Solution().groupThePeople(groupSizes=[3, 3, 3, 3, 3, 1, 3])
    assert [5] in sol
    assert [0, 1, 2] in sol
    assert [3, 4, 6] in sol

    sol = Solution().groupThePeople(groupSizes=[2, 1, 3, 3, 3, 2])
    assert [1] in sol
    assert [0, 5] in sol
    assert [2, 3, 4] in sol
