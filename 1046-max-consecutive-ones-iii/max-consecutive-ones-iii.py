class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        num_zeroes = 0
        max_w = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeroes += 1

            while num_zeroes > k:
                if nums[l] == 0:
                    num_zeroes -= 1
                l += 1

            max_w = max(max_w, r - l + 1)

        return max_w
            

            

            

