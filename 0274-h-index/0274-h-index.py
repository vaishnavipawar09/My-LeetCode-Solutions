class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)      #Sort in the descending order (6, 5, 3, 1, 0)
        for i in range(len(citations)):     #traverse through the whole array
            if citations[i] < i+1:         #true then return i, have atleast i+1 papers with i+1 or more citations.
                return i    #doesn’t have enough citations to support curr h-index val, return last 
                            #successful val(which is i).
        return len(citations) #If you make it through the whole list, then all papers support an h-index
        
    
#Time complexity : O(nlog n)
#Space Complexity: O()