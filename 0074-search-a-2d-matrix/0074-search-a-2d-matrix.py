class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n= len(matrix), len(matrix[0])       #Define dimension of matrix
        l = 0                                   #left and right ptr, right ptr is at the end of matrix
        r = (m * n) - 1

        while( l <= r):
            mid = (l + r) // 2                  #Cal mid val
            row = mid // n                      #Calculate the mid row of the matrix
            col = mid % n                       #Calculate mid column of matrix

            if matrix[row][col] < target:       #if target is greater shift the left ptr
                l = mid + 1
            elif matrix[row][col] > target:     #if target smaller than the mid matrix val, shift the right ptr
                r = mid - 1
            else:                               #If matrix[row][col] is equal to target return True
                return True                     #Target found

        return False                            #target not found

        #Time Complexity : O(log(m*n))
        #Space Complexity: O(1)

        