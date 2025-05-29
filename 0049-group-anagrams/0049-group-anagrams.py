class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)                 #Default list (hashmap), mapping chars cnt to list of anagrams
        for s in strs:                          #Go through the input string 
            count =[0] * 26                     #Count charaters (a .....z)
            for c in s:                         # Map the characters to the index
                count[ord(c) - ord("a")] += 1   #eg a=80, 80-80 = 0, maps it at 0, and later increments the counter
            res[tuple(count)].append(s)         #list cant be keys so tuple, as it is non muttable

        return list(res.values())               #return the anagrams grouped together

# Time Complexity : O( m * n * 26) = O(m*n), m is number of input string & n is the avg len of string 

# Space Complexity: O(m) extra space
#                   O(m * n ) space for the outut list        

"""
Method 1 Sorting 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

Time Complexity: O(m * nlog n)
Space Complexity: O(m * n)
"""