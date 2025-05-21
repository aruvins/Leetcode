class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        delete = 0
        maxSubarray = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                delete += 1

            while delete > 1:
                if nums[l] == 0:
                    delete -= 1
                l += 1

            maxSubarray = max((r-l) + 1, maxSubarray)

        return maxSubarray - 1