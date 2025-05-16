class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallestSeen = nums[0]
        secondSmallest = float('inf')

        for i in range(1,len(nums)):
            if nums[i] < smallestSeen:
                smallestSeen = nums[i]
            if nums[i] < secondSmallest and nums[i] > smallestSeen:
                secondSmallest = nums[i]
            if nums[i] > smallestSeen and nums[i] > secondSmallest:
                return True

        return False