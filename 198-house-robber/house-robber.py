class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i in memo:
                return memo[i]

            memo[i] = max(dfs(i - 1), nums[i] + dfs(i-2))
            return memo[i]

        
        return dfs(len(nums) - 1)