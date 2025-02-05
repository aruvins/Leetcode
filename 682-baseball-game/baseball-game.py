class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in range(len(operations)):
            if operations[i] == '+':
                a = stack[-1]
                b = stack[-2]
                stack.append(a+b)
            elif operations[i] == 'D':
                a = stack[-1]
                stack.append(2*a)
            elif operations[i] == 'C':
                stack.pop()
            else:
                stack.append(int(operations[i]))

        return sum(stack)






















# class Solution:
#     def calPoints(self, operations: List[str]) -> int:
#         stack = []

#         for i in range(len(operations)):
#             if operations[i] == "D":
#                 num1 = stack[-1]
#                 stack.append(num1 * 2)
#             elif operations[i] == "C":
#                 stack.pop()
#             elif operations[i] == "+":
#                 num1 = stack[-1]
#                 num2 = stack[-2]
#                 stack.append(num1 + num2)
#             else:
#                 stack.append(int(operations[i]))

#         return sum(stack)





























































        # stack = []
        # for i in range(len(operations)):
        #     if operations[i]=="D":
        #         stack.append(stack[-1]*2)
        #     elif operations[i]=="C":
        #         stack.pop(-1)
        #     elif operations[i]=="+":
        #         stack.append(stack[-1]+stack[-2])
        #     else:
        #         stack.append(int(operations[i]))
        # print(stack)
        # return sum(stack)