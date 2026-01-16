class Solution:
    def maximizeSquareArea(self, m, n, h, v):
        mod = 10**9 + 7
        s1, s2 = set(), set()
        h.extend([1, m])
        v.extend([1, n])
        h.sort()
        v.sort()

        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                s1.add(h[j] - h[i])

        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                s2.add(v[j] - v[i])

        ans = 0
        for i in s1:
            if i in s2:
                k = i * i
                ans = max(ans, k)

        if ans == 0:
            return -1
        return ans % mod