class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)
    
    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in range(1, 10):
                        if self.isValid(board, i, j, str(k)):
                            board[i][j] = str(k)
                            if self.solve(board):
                                return True
                        board[i][j] = '.'
                    return False
        return True
        
        
    def isValid(self, board, row, col, elem):
        
        for i in range(9):
            if board[row][i] == elem:
                return False
            
        for i in range(9):
            if board[i][col] == elem:
                return False
        
        subbox_x, subbox_y = row // 3 * 3, col // 3 * 3
        for i in range(3):
            for j in range(3):
                if board[subbox_x + i][subbox_y + j] == elem:
                    return False
                
        return True
    
    


# class Solution:
#     def solveSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: void Do not return anything, modify board in-place instead.
#         """
#         rows = [set([str(i) for i in range(1, 10)]) for _ in range(9)]
#         cols = [set([str(i) for i in range(1, 10)]) for _ in range(9)]
#         subboxes = [set([str(i) for i in range(1, 10)]) for _ in range(9)]
#         empty_cells = set()
        
#         for i, row in enumerate(board):
#             for j, elem in enumerate(row):
#                 if elem != '.':
#                     rows[i].remove(elem)
#                     cols[j].remove(elem)
#                     subboxes[i // 3 * 3 + j // 3].remove(elem)
#                 else:
#                     empty_cells.add((i, j))
                    
#         self.helper(rows, cols, subboxes, empty_cells, board)
        
#         return board

#     def isValidSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: bool
#         """
#         rows = [set() for _ in range(9)]
#         cols = [set() for _ in range(9)]
#         subboxes = [set() for _ in range(9)]
        
#         for i, row in enumerate(board):
#             for j, elem in enumerate(row):
#                 if elem == '.': continue
#                 if elem in rows[i]: return False
#                 if elem in cols[j]: return False
#                 if elem in subboxes[i // 3 * 3 + j // 3]: return False
#                 rows[i].add(elem)
#                 cols[j].add(elem)
#                 subboxes[i // 3 * 3 + j // 3].add(elem)
                
#         return True
                    
        
#     def helper(self, rows, cols, subboxes, empty_cells, board):
#         if not empty_cells:
#             return True

#         while empty_cells:
#             # print(empty_cells)
#             i, j = empty_cells.pop()
#             candidates = rows[i] & cols[j] & subboxes[i // 3 * 3 + j // 3]
#             if not candidates:
#                 empty_cells.add((i, j))
#                 return False
#             valid = False
#             for candidate in candidates:
#                 board[i][j] = candidate
#                 # if not self.isValidSudoku(board):
#                 #     empty_cells.add((i, j))
#                 #     return False
#                 rows[i].remove(candidate)
#                 cols[j].remove(candidate)
#                 subboxes[i // 3 * 3 + j // 3].remove(candidate)
#                 if self.helper(rows, cols, subboxes, empty_cells, board):
#                     valid = True
#                     break
#                 rows[i].add(candidate)
#                 cols[j].add(candidate)
#                 subboxes[i // 3 * 3 + j // 3].add(candidate)
#             if not valid:
#                 empty_cells.add((i, j))
#                 return False
            
#         return True
                    
                
sol = Solution()
test = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
sol.solveSudoku(test)
print(test)
