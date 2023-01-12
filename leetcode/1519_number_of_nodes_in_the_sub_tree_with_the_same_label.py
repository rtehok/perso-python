import collections
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        ans = [0] * n

        def dfs(node, parent, ans):
            node_count = [0] * 26
            node_count[ord(labels[node]) - ord('a')] = 1

            for child in graph[node]:
                if child == parent:
                    continue

                child_counts = dfs(child, node, ans)

                for i in range(26):
                    node_count[i] += child_counts[i]

            ans[node] = node_count[ord(labels[node]) - ord('a')]
            return node_count

        dfs(0, -1, ans)

        return ans


if __name__ == "__main__":
    assert Solution().countSubTrees(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], labels="abaedcd") == [2,1,1,1,1,1,1]
    assert Solution().countSubTrees(n=4, edges=[[0, 1], [1, 2], [0, 3]], labels="bbbb") == [4,2,1,1]
    assert Solution().countSubTrees(n=5, edges=[[0, 1], [0, 2], [1, 3], [0, 4]], labels="aabab") == [3,2,1,1,1]
