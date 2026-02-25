class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # I've taken 15 buckets here because max num in arr according to constraint is 10000, 
        # Use 32 buckets to represent 32 bits if constraint is bigger
        buckets = [[] for _ in range(15)]
        res = []

        # Calculating number of ones and placing the num in corresponding bucket
        for n in arr:
            nn = n
            ones = 0

            while n:
                n = n & (n - 1)
                ones += 1

            buckets[ones].append(nn)
        
        # Extracting result
        for buck in buckets:
            buck.sort()

            for n in buck:
                res.append(n)

        return res
        
        