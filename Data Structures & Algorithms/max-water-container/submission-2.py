class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # using a two pointer approach starting at diffrent ends
        result = 0
        l, r = 0, len(heights) - 1 

        # loop until the pointers meet before they cross each other 
        while l < r:
            # compute the area and we will use the bottlneck as our height value
            area = (r - l) * min(heights[l], heights[r])
            # we return the max since we are getting the max area 
            result = max(area,result)

            if heights[r] > heights[l]:
                l += 1 

            elif heights[r] < heights[l]:
                r -= 1 
            # which pointer we move if both the values are equal wouldn't matter in this case
            else:
                r -= 1

        return result