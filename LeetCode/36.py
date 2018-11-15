class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subboxes = [set() for _ in range(9)]
        
        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                if elem == '.': continue
                if elem in rows[i]: return False
                if elem in cols[j]: return False
                if elem in subboxes[i // 3 * 3 + j // 3]: return False
                rows[i].add(elem)
                cols[j].add(elem)
                subboxes[i // 3 * 3 + j // 3].add(elem)
                
        return True