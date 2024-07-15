from typing import List, Optional

from leetcode.helpers.helpers import TreeNode, is_same_tree, build_tree


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        children = set()
        for parent_val, child_val, is_left in descriptions:
            if parent_val not in node_map:
                node_map[parent_val] = TreeNode(parent_val)
            if child_val not in node_map:
                node_map[child_val] = TreeNode(child_val)

            if is_left:
                node_map[parent_val].left = node_map[child_val]
            else:
                node_map[parent_val].right = node_map[child_val]

            children.add(child_val)

        for node in node_map.values():
            if node.val not in children:
                return node

        return None


assert is_same_tree(Solution().createBinaryTree([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]),
                    build_tree([50, 20, 80, 15, 17, 19]))
assert is_same_tree(Solution().createBinaryTree([[1, 2, 1], [2, 3, 0], [3, 4, 1]]),
                    build_tree([1, 2, None, None, 3, 4]))
