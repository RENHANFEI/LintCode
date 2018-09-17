class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        if len(words) == 0 or len(words) == 1:
            return True
            
        for i in range(1, len(words)):
            for j in range(i, len(words)):
                if words[i][j] != words[j][i]:
                    return False
        
        return True
