from leetcode.helpers.helpers import TreeNode, build_tree, is_same_tree


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        node_sum = 0
        stack = []
        node = root

        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.right

            node = stack.pop()

            node_sum += node.val
            node.val = node_sum

            node = node.left

        return root


root = build_tree([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
Solution().bstToGst(root)
assert is_same_tree(root, build_tree([30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]))

root = build_tree([0, None, 1])
Solution().bstToGst(root)
assert is_same_tree(root, build_tree([1, None, 1]))
