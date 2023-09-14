import collections
from typing import List


class Solution:
    def findItineraryDFS(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for from_airport, to_airport in sorted(tickets, reverse=True):
            graph[from_airport].append(to_airport)

        res = []

        def dfs(curr_airport):
            while graph[curr_airport]:
                dfs(graph[curr_airport].pop())
            res.append(curr_airport)

        dfs("JFK")

        return res[::-1]

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        stack = ["JFK"]
        res = []

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            res.append(stack.pop())

        return res[::-1]


if __name__ == "__main__":
    assert Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == ["JFK", "MUC",
                                                                                                          "LHR", "SFO",
                                                                                                          "SJC"]
    assert Solution().findItinerary(
        [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]) == ["JFK", "ATL",
                                                                                              "JFK", "SFO",
                                                                                              "ATL", "SFO"]
