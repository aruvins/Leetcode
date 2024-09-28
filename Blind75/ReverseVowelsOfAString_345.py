# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for c in s:
            if (c == 'a' or c =='A') or (c == 'e' or c =='E') or (c == 'i' or c =='I') or (c == 'o' or c =='O') or (c == 'u' or c =='U'):
                vowels.append(c)

        vowels.reverse()
        res = ''
        i = 0
        for c in s:
            if c.lower() in 'aeiou':  
                if i < len(vowels):
                    res += vowels[i]
                    i += 1
                else:
                    res += c
            else:
                res += c

        return res