class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # https://keithschwarz.com/interesting/code/?dir=find-duplicate
        slow, fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        finder = 0

        while True:
            slow = nums[slow]
            finder = nums[finder]

            if slow == finder:
                return slow