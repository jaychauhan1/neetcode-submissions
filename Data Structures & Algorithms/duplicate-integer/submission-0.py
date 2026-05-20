class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we are already using a comparison so we don't need to give an if else statement 
        # if we put nums in a set it would be [1,2,3] and nums is currently [1,2,3,4] so if these set values
        #differ this means we have some valeus that appera more than once 
        return len(nums) != len(set(nums))


        