class Solution:
    def isValid(self, s: str) -> bool:
        endings = {'}':'{', ')': '(', ']':'['}
        stack = []

        for c in s:
            if c in endings:
                if stack and stack[-1] == endings[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack