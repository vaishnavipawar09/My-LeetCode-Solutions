class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        # Step 1: Reverse the whole array
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Step 2: Reverse first k elements
        l, r = 0, k - 1         #reverse from start to k 
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # Step 3: Reverse the rest
        l, r = k, len(nums) - 1  #reverse from k to end of array
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

#time Complexity: O(n)
#Space Complexity: O(1)