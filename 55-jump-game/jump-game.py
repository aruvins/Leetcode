class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalPost = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goalPost:
                goalPost = i

        return True if goalPost == 0 else False