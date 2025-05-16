class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallestSeen = float('inf')
        secondSmallest = float('inf')

        for i in range(len(nums)):
            if nums[i] <= smallestSeen:
                smallestSeen = nums[i]
            elif nums[i] <= secondSmallest:
                secondSmallest = nums[i]
            else:
                return True

        return False