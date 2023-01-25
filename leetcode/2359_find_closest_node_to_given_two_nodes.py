import math
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        dist1 = [math.inf] * n
        dist2 = [math.inf] * n

        dist1[node1], dist2[node2] = 0, 0

        visit1 = [False] * n
        visit2 = [False] * n

        def dfs(node, dist, visit):
            visit[node] = True
            neighbor = edges[node]
            if neighbor != -1 and not visit[neighbor]:
                dist[neighbor] = dist[node] + 1
                dfs(neighbor, dist, visit)

        dfs(node1, dist1, visit1)
        dfs(node2, dist2, visit2)

        min_dist_node = -1
        min_dist_till_now = math.inf

        for cur_node in range(n):
            #  Return the index of the node that can be reached from both node1 and node2, such that the maximum
            #  between the distance from node1 to that node, and from node2 to that node is minimized
            if min_dist_till_now > max(dist1[cur_node], dist2[cur_node]):
                min_dist_node = cur_node
                min_dist_till_now = max(dist1[cur_node], dist2[cur_node])

        return min_dist_node


if __name__ == "__main__":
    assert Solution().closestMeetingNode(edges=[2, 2, 3, -1], node1=0, node2=1) == 2
    assert Solution().closestMeetingNode(edges=[1, 2, -1], node1=0, node2=2) == 2
