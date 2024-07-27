import heapq
from typing import List


class Solution:
    def minimumCostDijkstra(self, source: str, target: str, original: List[str], changed: List[str],
                            cost: List[int]) -> int:
        n = len(original)
        graph = [[] for _ in range(26)]

        for i in range(n):
            graph[ord(original[i]) - ord("a")].append((ord(changed[i]) - ord("a"), cost[i]))

        def dijkstra(start_char) -> list[int]:
            pq = [(0, start_char)]
            min_costs = [float("inf")] * 26

            while pq:
                curr_cost, curr_char = heapq.heappop(pq)
                if min_costs[curr_char] != float("inf"):
                    continue

                min_costs[curr_char] = curr_cost

                for target_char, conversion_cost in graph[curr_char]:
                    new_total_cost = curr_cost + conversion_cost

                    if min_costs[target_char] == float("inf"):
                        heapq.heappush(pq, (new_total_cost, target_char))
            return min_costs

        min_conversion_costs = [dijkstra(i) for i in range(26)]

        total_cost = 0

        for s, t in zip(source, target):
            if s != t:
                char_conversion_cost = min_conversion_costs[ord(s) - ord("a")][ord(t) - ord("a")]
                if char_conversion_cost == float("inf"):
                    return - 1
                total_cost += char_conversion_cost

        return total_cost

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        min_cost_matrix = [[float("inf")] * 26 for _ in range(26)]

        for orig, chg, cst in zip(original, changed, cost):
            min_cost_matrix[ord(orig) - ord("a")][ord(chg) - ord("a")] = min(
                min_cost_matrix[ord(orig) - ord("a")][ord(chg) - ord("a")], cst
            )

        def floyd():
            for k in range(26):
                for i in range(26):
                    for j in range(26):
                        min_cost_matrix[i][j] = min(min_cost_matrix[i][j],
                                                    min_cost_matrix[i][k] + min_cost_matrix[k][j])

        floyd()

        total_cost = 0
        for s, t in zip(source, target):
            if s != t:
                char_conversion_cost = min_cost_matrix[ord(s) - ord("a")][ord(t) - ord("a")]
                if char_conversion_cost == float("inf"):
                    return -1
                total_cost += char_conversion_cost

        return total_cost


assert Solution().minimumCost(source="abcd", target="acbe", original=["a", "b", "c", "c", "e", "d"],
                              changed=["b", "c", "b", "e", "b", "e"], cost=[2, 5, 5, 1, 2, 20]) == 28

assert Solution().minimumCost(source="aaaa", target="bbbb", original=["a", "c"], changed=["c", "b"], cost=[1, 2]) == 12
assert Solution().minimumCost(source="abcd", target="abce", original=["a"], changed=["e"], cost=[10000]) == -1
