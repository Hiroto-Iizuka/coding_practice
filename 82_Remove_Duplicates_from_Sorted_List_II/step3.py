class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        delete_point = sentinel = ListNode(next=head)
        node = head

        while node and node.next:
            if node.val == node.next.val:
                while node.next and node.val == node.next.val:
                    node = node.next
                delete_point.next = node.next
            else:
                delete_point = delete_point.next
            node = node.next

        return sentinel.next
