class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = {}

        for x in nums:
            freq[x] = freq.get(x,0) + 1

        count = 0
        for i in range(3):
            for key in range(freq.get(i,0)):
                nums[count] = i
                count += 1 

            



