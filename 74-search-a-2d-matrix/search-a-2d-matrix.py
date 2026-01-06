class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            m = (top + bottom) // 2

            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bottom = m - 1
            else:
                row = m
                break
        else:
            return False

            
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            m = (l + r) // 2

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True

        return False