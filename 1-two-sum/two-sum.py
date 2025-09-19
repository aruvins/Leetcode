class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} #number: index

        for n in range(len(nums)):
            if target - nums[n] in hashMap:
                return [hashMap[target - nums[n]], n]

            hashMap[nums[n]] = n

        return -1


        
