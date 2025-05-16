class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallestSeen = secondSmallest = float('inf')

        for n in nums:
            if n <= smallestSeen:
                smallestSeen = n
            elif n <= secondSmallest:
                secondSmallest = n
            else:
                return True

        return False