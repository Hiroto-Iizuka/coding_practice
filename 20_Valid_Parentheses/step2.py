class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []
        
        for char in s:
            if char in bracket_pairs:
                stack.append(char)
            elif not stack or bracket_pairs[stack.pop()] != char:
                return False
        
        return len(stack) == 0
    