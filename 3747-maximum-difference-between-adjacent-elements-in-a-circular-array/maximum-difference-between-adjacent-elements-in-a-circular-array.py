class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxDifference = abs(nums[0] - nums[-1])
        for i in range(len(nums) - 1):
            maxDifference = max(maxDifference, abs(nums[i] - nums[i+1]))

        return maxDifference