class solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        node = head

        while node is not None:
            if node in visited:
                return True    
            visited.add(node)
            node = node.next

        return False
    