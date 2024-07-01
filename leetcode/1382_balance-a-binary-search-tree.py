# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.helpers.helpers import TreeNode, build_tree, is_same_tree


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []

        def inorder_traversal(node):
            if not node:
                return

            inorder_traversal(node.left)
            inorder.append(node.val)
            inorder_traversal(node.right)

        def create_balanced_bst(start, end):
            if start > end:
                return None

            mid = start + (end - start) // 2
            left = create_balanced_bst(start, mid - 1)
            right = create_balanced_bst(mid + 1, end)

            node = TreeNode(inorder[mid], left, right)
            return node

        inorder_traversal(root)
        return create_balanced_bst(0, len(inorder) - 1)


is_same_tree(Solution().balanceBST(build_tree([1, None, 2, None, 3, None, 4, None, None])),
             build_tree([2, 1, 3, None, None, None, 4]))
is_same_tree(Solution().balanceBST(build_tree([2, 1, 3])), build_tree([2, 1, 3]))
