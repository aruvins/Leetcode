class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0:len(prefix)-1]

        return prefix
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # commonPrefix = ""

        # for i in range(len(strs[0])):
        #     for word in strs:
        #         if i == len(word) or word[i]!= strs[0][i]:
        #             return commonPrefix
        #     commonPrefix += strs[0][i]

        # return commonPrefix














        # res = ""

        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i == len(s) or s[i] != strs[0][i]:
        #             return res
        #     res += strs[0][i]
        # return res