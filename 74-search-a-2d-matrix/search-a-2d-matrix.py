class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            m = (top+bot)//2

            if target > matrix[m][0] and target < matrix[m][-1]:
                break
            elif target < matrix[m][0]:
                bot = m - 1
            else:
                top = m + 1

        row = (top+bot)//2

        l,r = 0, len(matrix[row]) - 1

        while l <= r:
            m = (l+r)//2

            if target == matrix[row][m]:
                return True
            elif target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1


        return False