class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(next=head)
        prev_node = sentinel
        node = head

        while node and node.next:
            if node.val == node.next.val:
                while node.next and node.val == node.next.val:
                    node = node.next             
                prev_node.next = node.next
            else:
                prev_node = prev_node.next
            node = node.next

        return sentinel.next
