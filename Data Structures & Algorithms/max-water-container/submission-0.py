class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0 

        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            result = max(area, result)

            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l +=1
        return result

        