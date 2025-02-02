class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsSet = set(jewels)
        num = 0

        for stone in stones:
            if stone in jewelsSet:
                num +=1
        return num






















        # jewel_set = set(jewels)
        # count = 0

        # for stone in stones:
        #     if stone in jewel_set:
        #         count += 1

        # return count