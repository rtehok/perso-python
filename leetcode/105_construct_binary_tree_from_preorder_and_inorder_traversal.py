from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {}

        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        preorder_index = 0

        def arrayToTree(left, right):
            nonlocal preorder_index
            if left > right:
                return None

            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1

            root.left = arrayToTree(left, inorder_index_map[root_value] - 1)
            root.right = arrayToTree(inorder_index_map[root_value] + 1, right)

            return root

        return arrayToTree(0, len(preorder) - 1)


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
