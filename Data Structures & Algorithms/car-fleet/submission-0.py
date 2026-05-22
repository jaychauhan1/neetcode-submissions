class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for p, s in zip(position, speed):
            t = (target - p) / s
            time.append((t,p))
        time.sort(key = lambda x: x[1], reverse = True)


        stack = []
        for tim in time:
            if not stack or tim[0] > stack[-1]:
                stack.append(tim[0])
        return len(stack)
        