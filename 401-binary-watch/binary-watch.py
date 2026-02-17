class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn == 0:
            return ['0:00']
        mask = (1 << 6) - 1
        q = (1 << turnedOn) - 1
        limit = q << (10 - turnedOn)
        res = []

        while q <= limit:
            min = q & mask
            hour = q >> 6

            if hour < 12 and min < 60:
                res.append(f'{hour}:{min:0>2}')
            r = q & -q
            n = q + r
            q = (((q^n) // r) >> 2) | n
        return res