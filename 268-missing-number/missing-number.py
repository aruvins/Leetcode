class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        numSet = set(nums)

        for i in range(n):
            if i not in numSet:
                return i

        return -1