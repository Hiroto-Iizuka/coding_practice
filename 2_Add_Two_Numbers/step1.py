class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_node = ListNode()
        l1_node = l1
        l2_node = l2
        carry_up_one = 0

        while l1_node and l1_node.next:
            sum_num = l1_node.val + l2_node.val + carry_up_one
            if sum_num > 10:
                carry_up_one = 1
                result_node.val = sum_num % 10
            else:
                carry_up_one = 0
                result_node.val = sum_num % 10
            result_node.next = result_node
            l1_node = l1_node.next
            l2_node = l2_node.next

        return result_node.next
    