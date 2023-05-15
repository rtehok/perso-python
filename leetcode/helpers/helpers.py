from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(lst):
    if not lst:
        return None

    root = TreeNode(lst[0])
    queue = [root]
    i = 1

    while i < len(lst):
        node = queue.pop(0)

        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)

        i += 1

        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)

        i += 1

    return root


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(nums):
    if not nums:
        return None

    head = ListNode(nums[0])
    curr = head

    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        curr.next = node
        curr = curr.next

    return head

def compare_linked_lists(head1, head2):
    curr1 = head1
    curr2 = head2

    while curr1 and curr2:
        if curr1.val != curr2.val:
            return False
        curr1 = curr1.next
        curr2 = curr2.next

    # If one list is longer than the other
    if curr1 or curr2:
        return False

    return True
