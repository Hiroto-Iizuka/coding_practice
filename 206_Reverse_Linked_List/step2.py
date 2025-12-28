class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        stack = []

        while node:
            stack.append(node)
            node = node.next

        reverse_node = sentinel = ListNode(next=node)
        while stack:
            popped_node = stack.pop()
            reverse_node.next = popped_node
            reverse_node = popped_node
            if not stack:
                reverse_node.next = None

        return sentinel.next