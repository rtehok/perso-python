from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree, is_same_tree


class Solution:
    # SC O(n)
    def recoverTreeV1(self, root: Optional[TreeNode]) -> None:
        arr = []

        def dfs(node):
            if node:
                dfs(node.left)
                arr.append(node)
                dfs(node.right)

        dfs(root)

        sorted_values = sorted(n.val for n in arr)

        for i, s in enumerate(sorted_values):
            arr[i].val = s

    def recoverTreeV2(self, root: Optional[TreeNode]) -> None:
        nodes = []

        def inorder(node):
            if node:
                inorder(node.left)
                nodes.append(node)
                inorder(node.right)

        def find_swapped():
            n = len(nodes)
            x, y = None, None

            for i in range(n - 1):
                if nodes[i].val > nodes[i + 1].val:
                    y = nodes[i + 1]

                    if x is None:
                        x = nodes[i]
                    else:
                        break

            return x, y

        inorder(root)
        n1, n2 = find_swapped()
        n1.val, n2.val = n2.val, n1.val

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Initialize pointers and other variables
        curr, prev = root, None
        first, second = None, None

        # Morris traversal to find the swapped nodes
        while curr:
            if not curr.left:
                # If there is no left child, visit the node
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev
                        second = curr
                    else:
                        second = curr
                prev = curr
                curr = curr.right
            else:
                # If there is a left child, find the rightmost node in the left subtree
                temp = curr.left
                while temp.right and temp.right != curr:
                    temp = temp.right
                if not temp.right:
                    # Create a threaded link from the rightmost node to the current node
                    temp.right = curr
                    curr = curr.left
                else:
                    # Remove the threaded link and visit the node
                    temp.right = None
                    if prev and prev.val > curr.val:
                        if not first:
                            first = prev
                            second = curr
                        else:
                            second = curr
                    prev = curr
                    curr = curr.right

        # Swap the values of the two nodes
        first.val, second.val = second.val, first.val


if __name__ == "__main__":
    a = build_tree([1, 3, None, None, 2])
    Solution().recoverTree(a)
    assert is_same_tree(a, build_tree([3, 1, None, None, 2]))
    a = build_tree([3, 1, 4, None, None, 2])
    Solution().recoverTree(a)
    assert is_same_tree(a, build_tree([2, 1, 4, None, None, 3]))
