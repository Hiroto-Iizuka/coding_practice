class Solution:
    def isValid(self, s: str) -> bool:
        BRACKET_PAIRS = {'(': ')', '[': ']', '{': '}'}
        open_bracket_stack = []
        
        for ch in s:
            if ch in BRACKET_PAIRS:
                open_bracket_stack.append(ch)
                continue
                
            if not open_bracket_stack:
                return False
            
            open_bracket = open_bracket_stack.pop()
            if BRACKET_PAIRS[open_bracket] != ch:
                return False

        return len(open_bracket_stack) == 0