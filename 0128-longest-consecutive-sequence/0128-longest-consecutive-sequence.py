class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)                          #Create a Hashset
        longest = 0                                 #Keep track of te longest sequence

        for num in numSet:                          #Iterate through the nums Array
            if (num - 1) not in numSet:             #Check if there is a start of sequence (left nighbour)
                length = 1                          #legth of sequence
                while (num + length) in numSet:     # num+len check the curr number
                    length += 1
                longest = max(length, longest)      #If we find longest sequence, update he longest seq
        return longest                              #Return the longest sequence


        #Time & Space Complexity: O(n)
        