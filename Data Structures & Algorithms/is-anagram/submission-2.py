from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the two 2 strings don't equal each other they cannot be anagrams
        if len(s) != len(t):
            return False


        # we can store the frequency of each letter in string s and add it to our vlaue 
        # we can store the frequency of each letter in string t and subtract it to our value
        # the idea is the if its a anagram all the vlaues for each char should reach 0
        dictionary = defaultdict(int)
        for char in s:
            dictionary[char] += 1

        for char in t:
            dictionary[char] -= 1 

        return all(val == 0 for val in dictionary.values())

        