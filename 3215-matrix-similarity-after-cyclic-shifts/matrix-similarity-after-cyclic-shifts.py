class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])

        k %= n # reduce k < n

        for i in range(m):
            for j in range(n):
                # if row is even, left shift
                if i % 2 == 0:
                    if mat[i][j] != mat[i][(j + k) % n]:
                        return False
                # if row is even, left shift
                else:
                    if mat[i][j] != mat[i][(j - k) % n]:
                        return False

        return True