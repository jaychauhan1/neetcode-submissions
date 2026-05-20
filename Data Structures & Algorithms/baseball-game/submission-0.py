class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                d = stack[-1] * 2
                stack.append(d)
            elif op == "+":
                add = stack[-1] + stack[-2]
                stack.append(add)
            else:
                stack.append(int(op))

                
        return sum(stack)

