class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        if "++" in s:
            next_moves = []
            for i in range(len(s)-1):
                if s[i] == "+" and s[i+1] == "+":
                    next_moves.append(s[:i] + "--" + s[i+2:])
            return next_moves
        else:
            return []

sol = Solution()

s = "++++"
print(sol.generatePossibleNextMoves(s))