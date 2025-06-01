class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Create Hashsets for all
        cols = collections.defaultdict(set)         #set represents values 
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)      #key =(r/3, c/3)

        for r in range(9):                          #sudoko row
            for c in range(9):                      #sudoko column
                if board[r][c] == ".":              #If empty skip it and move forward
                    continue
                #Check if there exists a duplicates
                if (board[r][c] in rows[r] or       #Values inside the current row
                    board[r][c] in cols[c] or       #Values inside the current column
                    board[r][c] in squares[(r // 3, c // 3)]):  #Values inside the current squares
                    return False                    #Contains Duplicates
                 #Add values in the Hashsets
                cols[c].add(board[r][c])           
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True                                 #No Duplicates, sudoko is valid

        #Time Complexity: O(n^2)
        #Space Complexity: O(n^2)

