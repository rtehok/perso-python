# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTreeV1(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post_order_index = len(postorder) - 1
        inorder_index_map = {val: i for i, val in enumerate(inorder)}

        def helper(left, right):
            nonlocal post_order_index, inorder_index_map
            if left > right:
                return None

            root_value = postorder[post_order_index]
            post_order_index -= 1

            root = TreeNode(root_value)

            inorder_pivot_index = inorder_index_map[root_value]
            root.right = helper(inorder_pivot_index + 1, right)
            root.left = helper(left, inorder_pivot_index - 1)
            return root

        return helper(0, len(postorder) - 1)

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not postorder:
            return None

        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index + 1:], postorder[index:-1])
        return root


if __name__ == "__main__":
    print(Solution().buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]))
    print(Solution().buildTree(inorder=[-1], postorder=[-1]))
