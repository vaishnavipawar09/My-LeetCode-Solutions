class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * (len(nums))                 #each position intial value of , be the en of input array

        prefix = 1                 #Start with 1
        for i in range(len(nums)): #Loop through the array for output array
            res[i] = prefix        #Take the prefix and put the value in the i position, store prefix to res op array              
            prefix *= nums[i]      #take input array value and multiplied by the prefix, store it into 

        postfix = 1                #Same thing as prefix, intialize the postfix to 1
        for i in range(len(nums) - 1, -1, -1):      #start from the last index, reverse order
            res[i] *= postfix      #Take the postfix, multiple with val present at i postion, store postfix to res op array
            postfix *= nums[i]     #take input array value and multiplied by the postfix, store it into 

        return res                  #retun the combined result of the output array


        #Time Complexity: O(n)
        #Space Complexity: O(1)

#Dry Run
# nums = 1, 2, 3, 4      prefix = 1, postfix = 1 res =[]
#Prefix:
# 1.prefix = 1,  i=0, res[0]= 1, prefix = 1 * 1 = 1                     res= [1, 1, 1, 1]
# 2. prefix = 1, i = 1, res[1] = 1, prefix= 1 * nums[1] = 1 *2 = 2      res = [1, 1,1, 1]
# 3. prefix= 2, i =2, res[2] = 2, prefix = 2 * nums[2] = 2 * 3 = 6      res =[1, 1, 2, 1]
# 4. prefix = 6, i =3, res[3] = 6, prefix = 6 * nums[3] = 6 *4 = 24     res= [1, 1, 2, 6]

#Postfix:
# 1. potfix = 1, res[3] = postfix * res[3] = 1 * 6 = 6, postfix = pof * nums[3] = 1 * 4 = 4         res = [1, 1, 2, 6]
# 2. postfix = 4, res[2] = postfix * res[2] = 4 * 2 = 8, postfix = pof * nums[2] = 4 * 3 = 12       res = [1, 1, 8, 6]
# 3. postfix = 12, res[1] = postfix * res[1] = 12 * 1 = 12, postfix = pof *nums[1] = 12 * 2 = 24    res = [1, 12, 8, 6]
# 4. postfix = 24, res[0] = postfix * res[0] = 24 * 1= 24, postfix = pof * nums[0] = 24 * 1 = 24    res = [24,12, 8, 6]

#return res that is [24, 12, 8, 6] th output we wanted