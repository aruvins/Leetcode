class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelSet = {'a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O', 'U'}
        vowels = []

        for i in range(len(s)):
            if s[i] in vowelSet:
                vowels.append(s[i])
        
        vowels = vowels[::-1]
        count = 0
        res = ''
        for c in range(len(s)):
            if s[c] in vowelSet:
                print(vowels[count])
                res += vowels[count]
                count += 1
            else:
                res += s[c]
        return res
