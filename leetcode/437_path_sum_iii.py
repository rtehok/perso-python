import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        self.dic = collections.defaultdict(int)
        self.dic[0] = 1

        def traverse(node, running_sum):
            if not node:
                return

            running_sum += node.val
            complement = running_sum - targetSum
            self.count += self.dic[complement]

            self.dic[running_sum] += 1
            traverse(node.left, running_sum)
            traverse(node.right, running_sum)
            self.dic[running_sum] -= 1

        traverse(root, 0)
        return self.count


if __name__ == "__main__":
    assert Solution().pathSum(TreeNode(10,
                                       TreeNode(5,
                                                TreeNode(3,
                                                         TreeNode(3),
                                                         TreeNode(-2)),
                                                TreeNode(3,
                                                         None,
                                                         TreeNode(1))),
                                       TreeNode(-3,
                                                None,
                                                TreeNode(11))
                                       ),
                              8) == 3

    assert Solution().pathSum(TreeNode(-2, None, TreeNode(-3)), -5) == 1
    assert Solution().pathSum(TreeNode(1, TreeNode(-2), TreeNode(-3)), -1) == 1
    assert Solution().pathSum(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5))))), 6) == 1
