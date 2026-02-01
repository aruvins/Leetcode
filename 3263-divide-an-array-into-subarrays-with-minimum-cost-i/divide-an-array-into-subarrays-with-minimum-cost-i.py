class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        for i in range(1, 3):
            m = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[m]:
                    m = j
            nums[i], nums[m] = nums[m], nums[i]

        return nums[0] + nums[1] + nums[2]