import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == -1:
            return stones[-1]

        stones = [-1*stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -1 * heapq.heappop(stones)
            y = -1 * heapq.heappop(stones)

            if x == y:
                continue
            else:
                heapq.heappush(stones, -1 * (x-y))

        return -1 * stones.pop() if stones else 0

            




