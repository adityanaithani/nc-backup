class Solution:
    def isValid(self, s: str) -> bool:
        # store chars in a stack
        # iterate through string by index
        # if opening, push into the stack
        # if closing, check for opening at top of stack
        # return false if not there
        stack = []
        matches = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in matches:
                if stack and stack[-1] == matches[char]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(char)

        return True if not stack else False