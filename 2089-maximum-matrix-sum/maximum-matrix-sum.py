class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        totalSum = 0
        minAbsVal = float('inf')
        negativeCount = 0

        for row in matrix:
            for val in row:
                totalSum += abs(val)
                if val < 0:
                    negativeCount += 1

                minAbsVal = min(minAbsVal, abs(val))

        if negativeCount % 2 != 0:
            totalSum -= 2 * minAbsVal

        return totalSum