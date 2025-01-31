class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointerS = 0

        if s == '':
            return True

        for c in t:
            if s[pointerS] == c:
                pointerS += 1
            if pointerS == len(s):
                return True

        return False

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # sPointer = 0
        # if s == '':
        #     return True
            
        # for c in t:
        #     if c == s[sPointer]:
        #         sPointer +=1
        #     if sPointer == len(s):
        #         return True

        # return False

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if s == '':
        #     return True

        # stack = []
        # for c in s:
        #     stack.append(c)

        # for i in range(len(t) -1 , -1, -1):
        #     if stack and t[i] == stack[-1]:
        #         stack.pop()
                
        # if not stack:
        #     return True
        # return False