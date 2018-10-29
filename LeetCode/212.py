from collections import defaultdict
from copy import deepcopy

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board:
            return
        
        m, n = len(board), len(board[0])
        ans = set()
        
        for word in words:
            find_word = False
            for i in range(m):
                if find_word: 
                    break
                for j in range(n):
                    visited = defaultdict(lambda: False)
                    if self.dfs(word, 0, visited, board, i, j):
                        ans.add(word)
                        find_word = True
                        break
                        
        return list(ans)
                        
    def dfs(self, word, idx, visited, board, i, j):
        if idx == len(word):
            return True
        
        if (i < 0 or i >= len(board) or
            j < 0 or j >= len(board[0]) or
            visited[(i, j)] or
            word[idx] != board[i][j]):
            return False
        
        visited[(i, j)] = True
        if self.dfs(word, idx + 1, deepcopy(visited), board, i + 1, j): return True
        if self.dfs(word, idx + 1, deepcopy(visited), board, i - 1, j): return True
        if self.dfs(word, idx + 1, deepcopy(visited), board, i, j + 1): return True
        if self.dfs(word, idx + 1, deepcopy(visited), board, i, j - 1): return True
        
        return False
        
        
        