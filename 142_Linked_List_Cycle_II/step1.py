class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        cur = head

        while cur:
            if cur in visited:
                return cur
            visited.add(cur)
            cur = cur.next

        return None
