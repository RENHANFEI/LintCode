class Solution:
    """
    @param board: a 2D integer array
    @return: the current board
    """
    def candyCrush(self, board):
        
        if not board:
            return board
            
        if len(board[0]) == 0:
            return board
            
        while self.delCandy(board):
            self.dropCandy(board)
            
        return board
    
    
    def delCandy(self, board):
        
        crushes = []
        
        if len(board[0]) >= 3:
            for i, row in enumerate(board):
                pre_candy = row[0]
                rep = 1
                for j, candy in enumerate(row[1:]):
                    if candy != 0 and candy == pre_candy:
                        rep += 1
                    else:
                        if rep >= 3:
                            for k in range(rep):
                                crushes.append((i, j - k))
                        rep = 1
                    pre_candy = candy
                if rep >= 3:
                    for k in range(rep):
                        crushes.append((i, j + 1 - k))
                        
        for j in range(len(board[0])):
            pre_candy = board[0][j]
            rep = 1
            for i in range(len(board) - 1):
                candy = board[i + 1][j]
                if candy != 0 and candy == pre_candy:
                    rep += 1
                else:
                    if rep >= 3:
                        for k in range(rep):
                            crushes.append((i - k, j))
                    rep = 1
                pre_candy = candy
            if rep >= 3:
                for k in range(rep):
                    crushes.append((i - k + 1, j))
        for crush in crushes:
            board[crush[0]][crush[1]] = 0
            
        return crushes != []
            
            
    def dropCandy(self, board):
        
        for j in range(len(board[0])):
            col = []
            for i in range(len(board)):
                candy = board[i][j]
                if candy != 0:
                    col.append(candy)
                    
            if len(col) < len(board):
                col = [0] * (len(board) - len(col)) + col
                for i in range(len(board)):
                    board[i][j] = col[i]