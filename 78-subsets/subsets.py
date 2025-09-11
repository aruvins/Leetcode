class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(index):
            if index == len(nums):
                return [[]]

            allSubsets = helper(index + 1)
            item = nums[index]
            moreSubsets = []

            for subset in allSubsets:
                newSubset = subset + [item]
                moreSubsets.append(newSubset)

            return allSubsets + moreSubsets

        return helper(0)