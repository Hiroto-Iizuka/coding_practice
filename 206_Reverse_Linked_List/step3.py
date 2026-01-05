class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        stack = []
        while node:
            stack.append(node)
            node = node.next

        sentinel = reversed_node = ListNode()
        while stack:
            popped_node = stack.pop()
            reversed_node.next = popped_node
            reversed_node = popped_node
            if not stack:
                reversed_node.next = None

        return sentinel.next