class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2                 #Assign two different variables
        total = len(nums1) + len(nums2)     #total of both arrays
        half = total // 2                   #half of both arrrays

        if len(B) < len(A):                 #Check if A array is smaller
            A, B = B, A                     #Then we swap both arraysif A is bigger

        l, r = 0, len(A) - 1                #Use two pointers
        while True:                         #run the loop for binary search
            i = (l + r) // 2                #cal mid value (ptr for A)
            j = half - i - 2   #ptr for B (subtract by 2 cause arrays are indexed starting from 0)

            #Left partiton for A (if i is still in bound, if out of bound use infinity)
            Aleft = A[i] if i >= 0 else float("-infinity") 
            #Right partition for A (if out of bound set to +ve inf)
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            #Left partition for B (if j is still in bound, if out of bound use infinity)
            Bleft = B[j] if j >= 0 else float("-infinity")  
            #Right partition for B (if out of bound set to +ve inf)           
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            if Aleft <= Bright and Bleft <= Aright: #Check if the parttion is correct
                if total % 2:                       #Check if we have odd number
                    return min(Aright, Bright)      #get that by taking the minimum
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 #if even, we take max + min//2
            elif Aleft > Bright:         #if Al is too big reduce the size of A(left partiton of A)
                r = i - 1   
            else:
                l = i + 1                 #increase the size of left partition of A


#Time Complexity: O(log(min(n, m)))
#Space Complexity: O(1)