class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {")":"(", "]":"[", "}": "{"}

        for p in s:
            # append all the opening values to the stack
            if p in lookup.values():
                stack.append(p)
            
            # if closing and opening math at the top of stack we pop
            elif stack and lookup[p] == stack[-1]:
                stack.pop()

            else:
                return False
        return stack == []

