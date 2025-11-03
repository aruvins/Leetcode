import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            stone1 = heapq.heappop(maxHeap) * -1
            stone2 = heapq.heappop(maxHeap) * -1
            heapq.heappush(maxHeap, (stone1 - stone2)*-1)

        return maxHeap[-1] * -1 if maxHeap else 0
