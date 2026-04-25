class Solution:
    def isValid(self, s: str) -> bool:
        closing = {
            ']': '[',
            ')': '(',
            '}': '{'
        }


        stack = []

        for char in s:            
            if char in closing and len(stack) and stack[-1] == closing[char]:
                stack.pop()
            
            else:
                stack.append(char)

        return len(stack) == 0