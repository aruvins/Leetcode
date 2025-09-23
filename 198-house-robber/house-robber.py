class Solution:
    def rob(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]

        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        
        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        # return dp[len(nums) - 1]

        memo = {}

        def dfs(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i in memo:
                return memo[i]

            memo[i] = max(dfs(i-1), nums[i] + dfs(i-2))
            return memo[i]

        return dfs(len(nums) - 1)
