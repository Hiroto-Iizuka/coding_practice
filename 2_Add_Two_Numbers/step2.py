class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = result_node = ListNode()
        l1_node = l1
        l2_node = l2
        carry = 0

        while l1_node or l2_node or carry != 0:
            val1 = l1_node.val if l1_node else 0
            val2 = l2_node.val if l2_node else 0
            total = val1 + val2 + carry
            if total >= 10:
                carry = 1
            else:
                carry = 0            
            result_node.next = ListNode(val=total % 10)
            result_node = result_node.next

            if l1_node:              
                l1_node = l1_node.next
            if l2_node:
                l2_node = l2_node.next

        return answer.next
    