class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1          # Last element of real nums1
        p2 = n - 1          # Last element of nums2
        p = m + n - 1       # End of nums1 (including space for nums2)

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:   #check if the nums are greaer in which array, update that and add it to nums1
                nums1[p] = nums1[p1]
                p1 -= 1                 #decrement the ptr, if aded to the nums1 array
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Copy any remaining elements from nums2 (if any)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

#time Complexity: O(n)
#Space Complexiy : O(1)