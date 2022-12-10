from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7

        tree_sum = 0

        # Calculate the sum for the whole tree
        def treeSum(node):
            nonlocal tree_sum
            if node:
                tree_sum += node.val
                treeSum(node.left)
                treeSum(node.right)

        treeSum(root)

        res = -1

        # Calculate: (tree_sum - sub_tree_sum) * sub_tree_sum for each node
        def helper(node) -> int:
            nonlocal res
            if node is None:
                return 0

            left = helper(node.left)
            right = helper(node.right)
            sub_tree_sum = left + right + node.val
            res = max(res, (tree_sum - sub_tree_sum) * sub_tree_sum)

            return sub_tree_sum

        helper(root)
        return res % MOD


if __name__ == "__main__":
    root = TreeNode(1,
                    TreeNode(2,
                             TreeNode(4),
                             TreeNode(5)),
                    TreeNode(3,
                             TreeNode(6)))
    assert Solution().maxProduct(root) == 110
    root = TreeNode(1,
                    None,
                    TreeNode(2,
                             TreeNode(3),
                             TreeNode(4,
                                      TreeNode(5),
                                      TreeNode(6))))
    assert Solution().maxProduct(root) == 90
