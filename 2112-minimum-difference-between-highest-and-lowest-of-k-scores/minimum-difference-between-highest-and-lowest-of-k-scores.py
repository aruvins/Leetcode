class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, k - 1
        minDiff = nums[r] - nums[l]

        while r < len(nums) - 1:
            r += 1
            l += 1
            minDiff = min(minDiff, nums[r] - nums[l])

        return minDiff
