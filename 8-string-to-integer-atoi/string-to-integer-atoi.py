class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        i = 0
        if s[0] in ("-", "+"):
            if s[0] == "-":
                sign = -1
            i += 1

        res = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            if res > (2**31 - 1 - digit)// 10:
                return 2**31 - 1 if sign == 1 else -2**31
            res = res * 10 + digit
            i += 1

        return sign * res
