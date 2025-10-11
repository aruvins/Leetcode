class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, curSum, minSum = 0, 0, float('inf')

        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                minSum = min(minSum, r - l + 1)
                curSum -= nums[l]
                l += 1
        
        return 0 if minSum == float('inf') else minSum