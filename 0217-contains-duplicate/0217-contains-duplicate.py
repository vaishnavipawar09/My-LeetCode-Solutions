class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Create a hashset
        hashset = set()

        for n in nums:
            if n in hashset:  #Check if n is a duplicate
                return True   #Found Duplicate
            hashset.add(n)    #Add values to the hashset
        return False          #No Duplicate