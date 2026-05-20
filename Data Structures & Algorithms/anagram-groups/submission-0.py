from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # here we have 2 options
        # we could just sort every charachter in the string but that would take too long
        # it would be better if we used a hashmap in this case

        hashmap = defaultdict(list) 
        # our key here would be the asc value for each character in the word  and out key would be the list of 
        # of anagrams that match this 
        for s in strs:
            count = [0] * 26 
            for c in s:
                count[ord(c) - ord("a")] += 1
            hashmap[tuple(count)].append(s)
        return list(hashmap.values())