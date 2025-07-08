class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)    #k value to exceed the len of nums         O(1)

        # Step 1: Reverse the whole array
        l, r = 0, len(nums) - 1                                 #O(n/2) = O(n) 
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Step 2: Reverse first k elements
        l, r = 0, k - 1         #reverse from start to k         O(k/2) = O(k)    
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Step 3: Reverse the rest
        l, r = k, len(nums) - 1  #reverse from k to end of array   O(n - k / 2) = O(n -k)
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

#time Complexity: O(n) ==== O(n + k + n - k) = O(2n ) = O(n)
#Space Complexity: O(1)

#Dry Run: nums = [1, 2, 3, 4, 5, 6, 7] k = 3
# 1. k = 3, l = 0, r = 6, )< 6 yes, [7, 2, 3, 4, 5, 6, 1], l = 1, r = 5
# 2. l = 1, r = 5, 1< 5 yes , [7, 6, 3, 4, 5, 2, 1] l = 2, r = 4
# 3. l - 2, r -4 , 2< 4 yes, [7, 6, 5, 4, 3, 2, 1] l = 3, r = 3
# 4. l = r = 3 3< 3 no while loop ends

#l = 0, r = 2, 0< 2 yes, [5, 6, 7, 4, 3, 2, 1], l = 1, r = 1
# l = r = 1 , 1< 1 no, while loop will end

#l = 3, r = 6, 3< 6 yes [5, 6, 7, 1, 3, 2, 4], l = 4, r = 5
# l = 4, r = 5 4< 5 yes [5, 6, 7, 1, 2, 3, 4] l = 5, r= 4
# l = r= 4 while loop ends 
