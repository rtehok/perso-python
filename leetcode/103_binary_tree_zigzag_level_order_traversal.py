import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque([])
        q.append(root)

        if not root:
            return []

        res = []

        left_to_right = 0
        while q:
            q_size = len(q)
            curr = []

            for i in range(q_size):
                node = q.popleft()
                if left_to_right % 2 == 0:
                    curr.append(node.val)
                else:
                    curr.insert(0, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            left_to_right = not left_to_right

            res.append(curr)

        return res


if __name__ == "__main__":
    assert Solution().zigzagLevelOrder(TreeNode(3,
                                                TreeNode(9),
                                                TreeNode(20, TreeNode(15), TreeNode(7)))) == [[3],
                                                                                              [20, 9],
                                                                                              [15, 7]]
    assert Solution().zigzagLevelOrder(TreeNode(1)) == [[1]]
    assert Solution().zigzagLevelOrder(None) == []
    assert Solution().zigzagLevelOrder(TreeNode(1,
                                                TreeNode(2, TreeNode(4)),
                                                TreeNode(3, None, TreeNode(5)))) == [[1], [3, 2], [4, 5]]
