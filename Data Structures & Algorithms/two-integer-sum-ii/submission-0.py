class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            # this means our sum is too big
            if curSum > target:
                r -= 1 
            # this menas our sum is too small
            elif curSum < target:
                l += 1
            # meaning we found our sum so we return the i absed indices
            else:
                return [l + 1, r + 1]



        