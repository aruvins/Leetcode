class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSubarray = float('-inf')

        for i in range(len(nums)):
            curSum += nums[i]
            maxSubarray = max(maxSubarray, curSum)

            if curSum < 0:
                curSum = 0

        return maxSubarray