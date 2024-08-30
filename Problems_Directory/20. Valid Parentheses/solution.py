class Solution:
    def isValid(self, s: str) -> bool:
        # Tc = O(n)
        # Sc = O(n), using hashMap
        stack = []
        colsedToOpen = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for c in s :
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif c == ')' or c == ']' or c == '}':
                if len(stack) == 0 or colsedToOpen[c] != stack[-1]:
                    return False
                else : 
                    stack.pop()
       # return True if not stack else False            
        return True if len(stack) == 0 else False            
