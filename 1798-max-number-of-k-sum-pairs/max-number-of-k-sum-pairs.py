class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r = 0, len(nums) - 1
        count = 0

        while l<r:
            if nums[r]+nums[l] == k:
                count +=1
                r -= 1
                l += 1
            elif nums[r]+nums[l] < k:
                l += 1
            elif nums[r]+nums[l] > k:
                r -= 1

        return count