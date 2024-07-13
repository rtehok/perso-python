from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        indices = list(range(n))
        res = []
        stack = []

        indices.sort(key=lambda x: positions[x])

        for curr in indices:
            if directions[curr] == "R":
                stack.append(curr)
            else:
                while stack and healths[curr] > 0:
                    top_index = stack.pop()
                    if healths[top_index] > healths[curr]:
                        healths[top_index] -= 1
                        healths[curr] = 0
                        stack.append(top_index)
                    elif healths[top_index] < healths[curr]:
                        healths[top_index] = 0
                        healths[curr] -= 1
                    else:
                        healths[curr] = 0
                        healths[top_index] = 0
        for i in range(n):
            if healths[i] > 0:
                res.append(healths[i])

        return res


assert Solution().survivedRobotsHealths(positions=[5, 4, 3, 2, 1], healths=[2, 17, 9, 15, 10], directions="RRRRR") == [
    2, 17, 9, 15, 10]
assert Solution().survivedRobotsHealths(positions=[3, 5, 2, 6], healths=[10, 10, 15, 12], directions="RLRL") == [14]
assert Solution().survivedRobotsHealths(positions=[1, 2, 5, 6], healths=[10, 10, 11, 11], directions="RLRL") == []
