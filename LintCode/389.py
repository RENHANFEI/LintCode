from collections import defaultdict
class Solution:
    """
    @param board: the board
    @return: whether the Sudoku is valid
    """
    def isValidSudoku(self, board):
        columns = [set() for _ in range(9)]
        subboxes = [set() for _ in range(9)]
        
        for i, row in enumerate(board):
            row_set = set()
            for j, elem in enumerate(row):
                if elem == '.':
                    continue
                # check in row
                if elem in row_set:
                    return False
                row_set.add(elem)
                # check in column
                if elem in columns[j]:
                    return False
                columns[j].add(elem)
                # check in subbox
                subbox =  subboxes[i//3 * 3 + j//3]
                if elem in subbox:
                    return False
                subbox.add(elem)
            
        return True
