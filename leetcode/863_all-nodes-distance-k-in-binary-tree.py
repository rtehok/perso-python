import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distanceKV1(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        arr = []

        def add_parent(cur, parent):
            if cur:
                cur.parent = parent
                add_parent(cur.left, cur)
                add_parent(cur.right, cur)

        add_parent(root, None)

        visit = set()

        def dfs(node, dist):
            if not node or node in visit:
                return

            visit.add(node)
            if dist == 0:
                arr.append(node.val)
                return

            dfs(node.parent, dist - 1)
            dfs(node.left, dist - 1)
            dfs(node.right, dist - 1)

        dfs(target, k)

        return arr

    def distanceKDFS(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)

        def build_graph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)

            if cur.left:
                build_graph(cur.left, cur)

            if cur.right:
                build_graph(cur.right, cur)

        build_graph(root, None)

        ans = []
        visit = {target.val}

        def dfs(cur, dist):
            if dist == k:
                ans.append(cur)
                return

            for next_val in graph[cur]:
                if next_val not in visit:
                    visit.add(next_val)
                    dfs(next_val, dist + 1)

        dfs(target.val, 0)

        return ans

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)

        def build_graph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)

            if cur.left:
                build_graph(cur.left, cur)

            if cur.right:
                build_graph(cur.right, cur)

        build_graph(root, None)

        q = collections.deque([(target.val, 0)])

        ans = []

        visit = {target.val}

        while q:
            cur, dist = q.popleft()

            if dist == k:
                ans.append(cur)

            for neighbor in graph[cur]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    q.append((neighbor, dist + 1))

        return ans


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                    TreeNode(1, TreeNode(0), TreeNode(8)))
    assert all(x in [7, 4, 1] for x in Solution().distanceK(root=root, target=root.left, k=2))
    root = TreeNode(1)
    assert Solution().distanceK(root=root, target=root, k=3) == []
