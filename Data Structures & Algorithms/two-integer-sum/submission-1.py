class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums): # we want to grab both the index and values
            complement = target - num
            if complement in hashmap:
                 # we want to retrun the value of that complement stored in our hashmap the index of that and out current index
                return [hashmap[complement], i]
            # if its not in our hashmap we want to add that numebr and its index
            hashmap[num] = i # add in the key and the corresponding index which will be our key

        