class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minSoFar = float('inf')
        res = []

        for i in range(1, len(arr)):
            curMin = arr[i] - arr[i - 1]
            minSoFar = min(minSoFar, curMin)

        for i in range(1, len(arr)):
            curMin = arr[i] - arr[i - 1]
            if curMin == minSoFar:
                res.append([arr[i - 1], arr[i]])

        return res