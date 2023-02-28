import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtreesStringRepr(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        cnt = collections.defaultdict(int)
        res = []

        def traverse(node):
            if not node:
                return ""
            repr = "(" + traverse(node.left) + ")" + str(node.val) + "(" + traverse(node.right) + ")"
            cnt[repr] += 1
            if cnt[repr] == 2:
                res.append(node)
            return repr

        traverse(root)
        return res

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        cnt = collections.defaultdict(int)
        triplet_to_id = {}
        res = []

        def traverse(node):
            if not node:
                return 0
            triplet = (traverse(node.left), node.val, traverse(node.right))
            if triplet not in triplet_to_id:
                triplet_to_id[triplet] = len(triplet_to_id) + 1
            id = triplet_to_id[triplet]
            cnt[id] += 1
            if cnt[id] == 2:
                res.append(node)

            return id

        traverse(root)
        return res


if __name__ == "__main__":
    print(Solution().findDuplicateSubtrees(
        TreeNode(
            1,
            TreeNode(2, TreeNode(4)),
            TreeNode(3, TreeNode(2, TreeNode(4)), TreeNode(4))
        )))
    # == [TreeNode(2, TreeNode(4)), TreeNode(4))]
    print(Solution().findDuplicateSubtrees(TreeNode(2, TreeNode(1), TreeNode(1))))
    # == [TreeNode(1)]
