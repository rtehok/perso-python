from leetcode.helpers.helpers import build_tree, TreeNode


def morris_inorder_traversal(root):
    curr = root
    res = []
    while curr:
        if not curr.left:
            # If the left child of the current node is null
            # then process the current node and move to the right child of the current node.
            res.append(curr.val)
            curr = curr.right
        else:
            # If the left child of the current node is not null
            # then find the rightmost node of the left subtree of the current node
            # This node is the inorder predecessor of the current node.
            pre = curr.left
            while pre.right and pre.right != curr:
                pre = pre.right
            if not pre.right:
                # If the right child of the inorder predecessor is null
                # then set it to the current node, set the current node to its left child, and go back to step 1.
                pre.right = curr
                curr = curr.left
            else:
                # If the right child of the inorder predecessor is not null
                # then it must already be equal to the current node.
                # This means that we have visited all the nodes in the left subtree of the current node
                # so we can process the current node and set its right child to null.
                # Then, we move to the right child of the current node and go back to step 1.
                pre.right = None
                res.append(curr.val)
                curr = curr.right

    return res


if __name__ == "__main__":
    assert morris_inorder_traversal(
        TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, None, TreeNode(6))), TreeNode(3))) == [4, 2, 5, 6, 1, 3]
