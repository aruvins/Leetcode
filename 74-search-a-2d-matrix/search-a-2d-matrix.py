class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        # First binary search to find correct row
        while top <= bot:
            m = (top + bot) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                row = m
                break
            elif matrix[m][0] > target:
                bot = m - 1
            else:
                top = m + 1
        else:
            return False  # No valid row found

        # Second binary search within the row
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1

        return False
