import collections
from typing import List


class Solution:
    def calcEquationDFS(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for i, (x, y) in enumerate(equations):
            graph[x][y] = values[i]
            graph[y][x] = 1 / values[i]

        res = []

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            visited.add(start)

            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return value * result

            return -1.0

        for dividend, divisor in queries:
            res.append(dfs(dividend, divisor, set()))

        return res

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)

        for (numerator, denominator), value in zip(equations, values):
            graph[numerator][denominator] = value
            graph[denominator][numerator] = 1.0 / value

        res = []

        for start, end in queries:
            if start not in graph or end not in graph:
                res.append(-1)
            elif start == end:
                res.append(1)
            else:
                q = collections.deque([(start, 1.0)])
                visited = set()

                found = False
                while q and not found:
                    curr, curr_value = q.popleft()
                    visited.add(curr)

                    for neighbor, neighbor_value in graph[curr].items():
                        if neighbor not in visited:
                            new_value = curr_value * neighbor_value
                            if neighbor == end:
                                res.append(new_value)
                                found = True
                                break
                            q.append((neighbor, new_value))

                if not found:
                    res.append(-1)
        return res


if __name__ == "__main__":
    assert Solution().calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                                   queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]) == [6.00000,
                                                                                                             0.50000,
                                                                                                             -1.00000,
                                                                                                             1.00000,
                                                                                                             -1.00000]
    assert Solution().calcEquation(equations=[["a", "b"], ["b", "c"], ["bc", "cd"]], values=[1.5, 2.5, 5.0],
                                   queries=[["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]) == [3.75000, 0.40000,
                                                                                                     5.00000, 0.20000]
    assert Solution().calcEquation(equations=[["a", "b"]], values=[0.5],
                                   queries=[["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]) == [0.50000, 2.00000,
                                                                                                 -1.00000, -1.00000]
