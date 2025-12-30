class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        last_fixed_node = dummy
        node = head

        while node and node.next:
            if node.val == node.next.val:
                while node.next and node.val == node.next.val:
                    node = node.next
                last_fixed_node.next = node.next
            else:
                last_fixed_node = last_fixed_node.next
            node = node.next

        return dummy.next
    