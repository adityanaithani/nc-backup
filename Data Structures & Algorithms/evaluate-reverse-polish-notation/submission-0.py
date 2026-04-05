class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # o(N) time and space
        # return integer that given expression evaluates to 
        
        # use a stack
        # collect numbers in stack
        # when operand reached, operate on the stack (ie. pop twice), clear it and add result, continue
        # return stack at the end

        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack.pop()