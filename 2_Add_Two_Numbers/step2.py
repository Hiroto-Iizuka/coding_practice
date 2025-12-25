class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        last_fixed = dummy

        n1 = l1
        n2 = l2
        carry = 0
        while n1 or n2 or carry != 0:
            val1 = n1.val if n1 else 0
            val2 = n2.val if n2 else 0
            total = val1 + val2 + carry
            if total >= 10:
                total -= 10
                carry = 1
            else:
                carry = 0

            last_fixed.next = ListNode(val=total)
            last_fixed = last_fixed.next

            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next

        return dummy.next
