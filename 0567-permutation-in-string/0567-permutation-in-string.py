class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        l=0
        counts1= {}
        counts2 = {}

        for c in s1:       # Expand window
            counts1[c] = 1 + counts1.get(c, 0)

        for r in range(len(s2)):
            counts2[s2[r]] = 1 + counts2.get(s2[r], 0)

            while (r - l + 1) > len(s1):
                counts2[s2[l]] -= 1
                if counts2[s2[l]] == 0:  
                    del counts2[s2[l]]
                l += 1

            if counts1 == counts2:
                return True

        return False                
        
#Time Complexity: O(n)   , n is len of s2 string
#Space Complexity: O(1)
        
        
        
        
        
   
   