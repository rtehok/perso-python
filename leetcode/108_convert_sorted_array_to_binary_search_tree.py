# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        middle = len(nums) // 2
        return TreeNode(nums[middle],
                        self.sortedArrayToBST(nums[:middle]),
                        self.sortedArrayToBST(nums[middle + 1:]))


if __name__ == "__main__":
    root = TreeNode(0, TreeNode(-3, TreeNode(-10)), TreeNode(9, TreeNode(5)))
    print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))
