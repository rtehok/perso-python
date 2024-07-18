# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import chain

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def countPairsV1(self, root: TreeNode, distance: int) -> int:
        leaves = set()
        graph = defaultdict(list)

        def traverse(node, prev):
            if node is None:
                return

            if node.left is None and node.right is None:
                leaves.add(node)

            if prev is not None:
                graph[prev].append(node)

            graph[node].append(prev)

            traverse(node.left, node)
            traverse(node.right, node)

        traverse(root, None)

        ans = 0
        for leaf in leaves:
            q = deque([leaf])
            seen = set([leaf])
            for _ in range(distance + 1):
                q_len = len(q)
                for _ in range(q_len):
                    curr = q.popleft()
                    if curr in leaves and curr != leaf:
                        ans += 1
                    if curr in graph:
                        for neighbor in graph.get(curr):
                            if neighbor not in seen:
                                seen.add(neighbor)
                                q.append(neighbor)

        return ans // 2

    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = 0

        def postorder(node, level):
            nonlocal res
            if not node:
                return []

            if node.left == node.right:
                return [1]

            left_dist = postorder(node.left, level + 1)
            right_dist = postorder(node.right, level + 1)

            for l in left_dist:
                if l > distance:
                    continue
                for r in right_dist:
                    res += l + r <= distance

            dist = []
            for d in chain(left_dist, right_dist):
                d += 1
                if d < distance:
                    dist.append(d)

            return dist

        postorder(root, 1)
        return res


assert Solution().countPairs(root=build_tree([1, 2, 3, None, 4]), distance=3) == 1
assert Solution().countPairs(root=build_tree([1, 2, 3, 4, 5, 6, 7]), distance=3) == 2
assert Solution().countPairs(root=build_tree([7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2]),
                             distance=3) == 1
