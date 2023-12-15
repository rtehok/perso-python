from typing import List


class Solution:
    def destCityV1(self, paths: List[List[str]]) -> str:
        outbound = collections.defaultdict(int)
        inbound = collections.defaultdict(int)

        for x, y in paths:
            inbound[y] += 1
            outbound[x] += 1

        for d, i in inbound.items():
            if i == 1:
                if outbound[d] == 0:
                    return d

        return ""

    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = set()
        for i in range(len(paths)):
            outgoing.add(paths[i][0])

        for i in range(len(paths)):
            candidate = paths[i][1]
            if candidate not in outgoing:
                return candidate

        return ""


assert Solution().destCity(paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]) == "Sao Paulo"
assert Solution().destCity(paths=[["B", "C"], ["D", "B"], ["C", "A"]]) == "A"
assert Solution().destCity(paths=[["A", "Z"]]) == "Z"
