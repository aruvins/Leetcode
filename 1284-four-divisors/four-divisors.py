class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        
        for num in nums:
            divisors = self.get_divisors(num)

            if(len(divisors) == 4):
                ans += sum(divisors)

        return ans

    def get_divisors(self, n):
        divisors = []
        limit = n ** 0.5
        i = 1

        while (i <= limit):
            if(n % i == 0):
                divisors.append(i)
                poss_div = n//i
                if(poss_div != i):
                    divisors.append(poss_div)

            i += 1

        return divisors
        