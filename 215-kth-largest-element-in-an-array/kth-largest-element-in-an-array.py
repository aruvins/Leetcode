import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        nums = [-1 * n for n in nums]
        heapq.heapify(nums)

        while k > 0:
            res.append(heapq.heappop(nums))
            k -= 1

        return res[-1] * -1