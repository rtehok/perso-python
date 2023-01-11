import collections
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent):
            total_time = 0

            # it's a leaf
            if node not in graph:
                return 0

            for child in graph[node]:
                if child == parent:
                    continue

                child_time = dfs(child, node)  # retrieve child time

                # If the child has an apple (hasApple[child] = true) or there are any apples in its subtree,
                # which can be checked if we need any time to collect apples (childTime > 0),
                # we must visit child, which takes one unit of time,
                # collect all apples in the child's subtree which takes childTime,
                # and return, which again takes one unit of time. So, we add childTime + 2 to the totalTime.
                if child_time > 0 or hasApple[child]:
                    total_time += child_time + 2

            return total_time

        return dfs(0, -1)


if __name__ == "__main__":
    assert Solution().minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                              hasApple=[False, False, True, False, True, True, False]) == 8
    assert Solution().minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                              hasApple=[False, False, True, False, False, True, False]) == 6
    assert Solution().minTime(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                              hasApple=[False, False, False, False, False, False, False]) == 0
