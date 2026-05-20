class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l, r = 0, len(heights) - 1 

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            result = max(area,result)

            if heights[r] > heights[l]:
                l += 1 

            elif heights[r] < heights[l]:
                r -= 1 

            else:
                r -= 1

        return result