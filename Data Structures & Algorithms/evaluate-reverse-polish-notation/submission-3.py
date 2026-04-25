class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        """

        stack = []

        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                right = stack.pop()
                left = stack.pop()
                new_val = 0
                if token == '+':
                    new_val = left + right
                    
                elif token == '-':
                    new_val = left - right
                    
                elif token == '*':
                    new_val = left * right
                    
                else:
                    new_val = int(left / right)
            
                stack.append(new_val)

            else:
                stack.append(int(token))
            
        return stack[0] if len(stack) else -1