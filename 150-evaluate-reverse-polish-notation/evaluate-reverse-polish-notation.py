class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for e in tokens:
            if e == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)
            elif e == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y - x)
            elif e == "*":
                x = stack.pop()
                y = stack.pop()
                stack.append(x*y)
            elif e == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y/x))
            else:
                stack.append(int(e))
                
        return stack[-1]