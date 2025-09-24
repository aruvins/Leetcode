class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)

        time = 0

        while heap:
            i = 0
            temp = []
            while i <= n:
                if heap:
                    count = heapq.heappop(heap)
                    if count + 1 < 0:
                        temp.append(count + 1)
                time += 1
                if not heap and not temp:
                    break
                i += 1
            for item in temp:
                heapq.heappush(heap, item)

        return time