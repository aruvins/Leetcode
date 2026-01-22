class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_non_decreasing(nums):
            return all(nums[i] >= nums[i - 1] for i in range(1, len(nums)))

        ops = 0

        while not is_non_decreasing(nums):
            min_sum = float('inf')
            idx = 0

            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            nums = nums[:idx] + [nums[idx] + nums[idx + 1]] + nums[idx + 2:]
            ops += 1

        return ops
