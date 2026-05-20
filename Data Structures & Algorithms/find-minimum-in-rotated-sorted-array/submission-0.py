class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,1,2]
        # [1,2,3,4,5]
        #  l   m   r 

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            # we want to seatch the right side for the minimum
            if nums[m] >= nums[r]:
                l = m + 1
            else:
                # search the left right side
                # becaus the minimum is either at m or to the left of it
                r = m
        return nums[l]

        




        