from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def helper(left, right):
            if left == right:
                return None

            slow, fast = left, left
            while fast != right and fast.next != right:
                slow = slow.next
                fast = fast.next.next

            root = TreeNode(slow.val)
            root.left = helper(left, slow)
            root.right = helper(slow.next, right)
            return root

        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        return helper(head, None)


if __name__ == "__main__":
    root = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
    print(Solution().sortedListToBST(root))
