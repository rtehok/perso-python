from typing import Optional

from leetcode.helpers.helpers import ListNode, build_list, compare_linked_lists


class Solution:
    def removeNodesStack(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = stack.pop()
        maximum = curr.val
        result_list = ListNode(maximum)

        while stack:
            curr = stack.pop()
            if curr.val < maximum:
                continue

            else:
                new_node = ListNode(curr.val)
                new_node.next = result_list
                result_list = new_node
                maximum = curr.val

        return result_list

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        next_node = self.removeNodes(head.next)

        if head.val < next_node.val:
            return next_node

        head.next = next_node
        return head


assert compare_linked_lists(Solution().removeNodes(build_list([5, 2, 13, 3, 8])), build_list([13, 8]))
assert compare_linked_lists(Solution().removeNodes(build_list([1, 1, 1, 1])), build_list([1, 1, 1, 1]))
