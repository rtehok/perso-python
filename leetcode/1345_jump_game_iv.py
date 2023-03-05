import collections
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        if n <= 1:
            return 0

        graph = collections.defaultdict(list)
        for i, num in enumerate(arr):
            graph[num].append(i)

        q = collections.deque([])
        q.append(([0], 0))
        visited = {0}

        while q:
            nodes, step = q.popleft()
            nex = []
            for node in nodes:
                if node == n - 1:
                    return step

                # check same value
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                # check neighbors
                for child in [node - 1, node + 1]:
                    if 0 <= child < n and child not in visited:
                        visited.add(child)
                        nex.append(child)

            q.append((nex, step + 1))

        return -1


if __name__ == "__main__":
    assert Solution().minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]) == 3
    assert Solution().minJumps([7]) == 0
    assert Solution().minJumps([7, 6, 9, 6, 9, 6, 9, 7]) == 1
