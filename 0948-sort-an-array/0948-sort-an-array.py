class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #return sorted(nums) Works but the question states do not use built in!

        #Merge function

        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1] # does not include the last value hence used + 1
            i, j, k = L, 0 , 0 # i is for arr, j and k are the pointers at the beginning of the subarrays
            
            while j < len(left) and k< len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j +=1
                else:
                    arr[i] = right[k]
                    k+=1
                i += 1 # Irrespective of j and k , i should get incremented

            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1


        # Using Merge sort  
        def mergesort(arr, l, r):
            if l ==r:
                return arr

            m = (l + r) // 2  # mid
            mergesort(arr, l, m) # Left half
            mergesort(arr, m+1, r) # Right Half 
            merge(arr, l, m, r) # Merge 
            return arr
        
        return mergesort(nums, 0, len(nums)- 1)

