class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # for i in range(len(nums)):
        #     if sum(nums[:i]) == sum(nums[i+1:]):
        #         return i
        
        # return -1

        total = sum(nums)
        left_total = 0

        for i in range(len(nums)):
            right_total = total - left_total - nums[i]

            if left_total == right_total:
                return i

            left_total += nums[i]

        return -1