class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        existsSet = set()

        for n in nums:
            if n in existsSet:
                return True
            existsSet.add(n)

        return False

























        # num_set = set()

        # for n in nums:
        #     if n in num_set:
        #         return True
        #     else:
        #         num_set.add(n)

        # return False
