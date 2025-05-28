class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map ={}                           #Create a HashMap to store the values
        
        for i, n in enumerate(nums):
            diff = target - n               #To check if the diff exits in hashmap
            if diff in h_map:               #If yes than return index
                return [h_map[diff], i]
            h_map[n] = i                    #Store the value in the hashmap
        return 0

#Time Complexity: O(n) 
#Space Complexity: O(n)

    """ Brute Force Method:

    class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

Time Complexity : O(n^2), Space Complexity: O(1)

This above is the Brute force method, iterate through the whole array to find the target"""
        
        