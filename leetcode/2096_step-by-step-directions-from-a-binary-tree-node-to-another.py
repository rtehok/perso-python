from collections import deque
from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_start(node):
            if not node:
                return None

            if node.val == startValue:
                return node

            left_result = find_start(node.left)
            if left_result:
                return left_result

            return find_start(node.right)

        parent_map = {}

        def populate_parent_map(node):
            if not node:
                return

            if node.left:
                parent_map[node.left.val] = node
                populate_parent_map(node.left)

            if node.right:
                parent_map[node.right.val] = node
                populate_parent_map(node.right)

        path_tracker = {}

        def backtrack_path(node):
            path = []
            while node in path_tracker:
                path.append(path_tracker[node][1])
                node = path_tracker[node][0]
            path.reverse()
            return "".join(path)

        start_node = find_start(root)
        populate_parent_map(root)

        q = deque([start_node])
        visited = set()

        visited.add(start_node)

        while q:
            curr = q.popleft()

            if curr.val == destValue:
                return backtrack_path(curr)

            if curr.val in parent_map:
                parent_node = parent_map[curr.val]
                if parent_node not in visited:
                    q.append(parent_node)
                    path_tracker[parent_node] = (curr, "U")
                    visited.add(parent_node)
            if curr.left and curr.left not in visited:
                q.append(curr.left)
                path_tracker[curr.left] = (curr, "L")
                visited.add(curr.left)
            if curr.right and curr.right not in visited:
                q.append(curr.right)
                path_tracker[curr.right] = (curr, "R")
                visited.add(curr.right)

        return ""


assert Solution().getDirections(build_tree([5, 1, 2, 3, None, 6, 4]), 3, 6) == "UURL"
assert Solution().getDirections(build_tree([2, 1]), 2, 1) == "L"
