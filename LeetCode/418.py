class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        
        ans = 0
        idx_sentence = -1
        row = 0
        while row < rows:
            idx_col = 0
            if idx_sentence == 0:
                ans = rows // row * ans
                row = rows - rows % row
                if row >= rows:
                    break
            if idx_sentence == -1:
                idx_sentence = 0
            # if len(sentence) < cols:
            #     ans += cols // (len(' '.join(sentence)) + 1)
            while cols - idx_col >= len(sentence[idx_sentence]):
                idx_col += len(sentence[idx_sentence]) + 1
                idx_sentence += 1
                if idx_sentence == len(sentence):
                    idx_sentence = 0
                    ans += 1
            row += 1
        
        return ans


sol = Solution()
sentence = ["f","p","a"]
rows = 8
cols = 7

sentence = ["h"]
rows = 2
cols = 3
print(sol.wordsTyping(sentence, rows, cols))