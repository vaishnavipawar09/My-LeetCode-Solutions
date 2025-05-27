class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):                        #Check if both the strings are of same size
            return False
        
        cntS, cntT = {}, {}                         #Create Hashmap for both strings

        for i in range(len(s)):                     #Iterate through the string
            cntS[s[i]] = 1 + cntS.get(s[i], 0)      #Increate the count of the charatcter using .get, s[i] is the key
            cntT[t[i]] = 1 + cntT.get(t[i], 0)      # 0 is the default value
        return cntS == cntT

    
        #Time Comlexity: O(n + m),    Where n is the length of string s and m is the length of string t.
        #Space Complexity: O(1)