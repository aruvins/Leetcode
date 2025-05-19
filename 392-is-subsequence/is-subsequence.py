class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l,r = 0,0

        if s == "":
            return True

        while r < len(t):
            if s[l] == t[r]:
                l += 1
            if l >= len(s):
                return True
            r += 1

        return False