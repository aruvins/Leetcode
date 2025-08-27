class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # @cache
        # def solve(i, must_pick):
        #     if i >= len(nums):
        #         return 0 if must_pick else -inf
        #     return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))

        # return solve(0, False)

        curSum = nums[0]
        maxSum = nums[0]

        for n in nums[1:]:
            curSum = max(n, curSum + n)
            maxSum = max(curSum, maxSum)

        return maxSum