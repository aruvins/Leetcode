class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr = list(str(x))
        revArr = arr[::-1]

        return arr == revArr

            

