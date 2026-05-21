class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))

            elif token == "+":
                right = stack.pop()
                left = stack.pop()
                add = left + right
                stack.append(add)

            elif token == "-":
                right = stack.pop()
                left = stack.pop()
                subtract = left - right
                stack.append(subtract)

            elif token == "*":
                right = stack.pop()
                left = stack.pop()
                multiply = left * right
                stack.append(multiply)

            elif token == "/":
                right = stack.pop()
                left = stack.pop()
                divide = left / right
                stack.append(int(divide))
        
        return stack[-1]
