from typing import Optional

from leetcode.helpers.helpers import TreeNode, build_tree


class BSTIteratorV1:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = self._create_arr(root)[::-1]

    def next(self) -> int:
        return self.arr.next()

    def hasNext(self) -> bool:
        return len(self.arr)

    def _create_arr(self, node):
        if not node:
            return []
        return self._create_arr(node.left) + [node.val] + self._create_arr(node.right)


class BSTIteratorGenerator:
    def __init__(self, root: Optional[TreeNode]):
        self.iter = self._inorder(root)
        self.nxt = next(self.iter, None)

    def next(self) -> int:
        res, self.nxt = self.nxt, next(self.iter, None)
        return res

    def hasNext(self) -> bool:
        return self.nxt is not None

    def _inorder(self, node):
        if node:
            yield from self._inorder(node.left)
            yield node.val
            yield from self._inorder(node.right)


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)

    def next(self) -> int:
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left


if __name__ == "__main__":
    bst_it = BSTIterator(build_tree([7, 3, 15, None, None, 9, 20]))
    assert bst_it.next() == 3
    assert bst_it.next() == 7
    assert bst_it.hasNext()
    assert bst_it.next() == 9
    assert bst_it.hasNext()
    assert bst_it.next() == 15
    assert bst_it.hasNext()
    assert bst_it.next() == 20
    assert not bst_it.hasNext()
