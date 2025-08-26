class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_index = {}

        for i, val in enumerate(nums):
            if target - val in pair_index:
                return [i, pair_index[target- val]]
            pair_index[val] = i

        
