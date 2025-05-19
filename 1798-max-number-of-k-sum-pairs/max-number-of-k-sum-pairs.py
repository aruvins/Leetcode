class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hmap = {}
        count = 0

        for i in range(len(nums)):
            if hmap.get(k-nums[i],0) > 0:
                count += 1
                hmap[k-nums[i]] -= 1
            else:
                hmap[nums[i]] = hmap.get(nums[i], 0) + 1

        return count

