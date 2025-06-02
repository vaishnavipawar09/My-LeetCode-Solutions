class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []                                    #Return the result in the form of list hence []
        nums.sort()                                 #Sort the array

        i = 0                                       
        for i in range(len(nums)):                  #Iterates through the array
            if i > 0 and nums[i] == nums[i - 1]:    #If duplicates, move forward, i is at start 
                continue

            j, k = i + 1, len(nums) - 1             #Create left and right pointer, left is i +1, cause i!=j

            while j < k:
                calsum = nums[i] + nums[j] + nums[k] #Calculate the three sum
                if  calsum < 0:                     #Sum < 0, increase the left pointer by 1
                    j += 1
                elif calsum > 0:                    #Sum > 0, decrease the right pointer by 1
                    k -=1
                else:                               #If sum == 0, add the values in the array
                    res.append([nums[i], nums[j], nums[k]]) # add to te result
                    j += 1                          #Update the pointers j and k
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]: #Duplicate, so shift our pointer
                        j += 1
                    
        return res                                  #return the result


#Time Complexity: O(n^2)    (one loop takes nlog n and the other j, k loop takes n^2 so total it is n^2)
#Space Complexity: O(1) or O(n) depends upon sorting algorithm

    
