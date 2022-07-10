from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # res = []
        #
        # q = deque()
        # q.append([root, 0])
        #
        # while q:
        #     node, level = q.popleft()
        #
        #     if len(res) <= level:
        #         res.append([node.val])
        #     else:
        #         res[level].append(node.val)
        #
        #     if node.left:
        #         q.append([node.left, level + 1])
        #     if node.right:
        #         q.append([node.right, level + 1])
        #
        # return res
        if not root:
            return []

        res = []

        def dfs(node, level):
            if len(res) <= level:
                res.append([node.val])
            else:
                res[level].append(node.val)

            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        dfs(root, 0)

        return res


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert Solution().levelOrder(root) == [[3], [9, 20], [15, 7]]
    root = TreeNode(1)
    assert Solution().levelOrder(root) == [[1]]
