class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = []
        for c in s:
            if c.isalnum():
                filtered.append(c.lower())

        string = ''.join(filtered)

        l, r = 0, len(string) - 1

        while l <= r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1

        return True