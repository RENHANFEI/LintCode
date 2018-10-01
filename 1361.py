import math

class Solution:
    """
    @param words: an array of string
    @param maxWidth: a integer
    @return: format the text such that each line has exactly maxWidth characters and is fully
    """
    def fullJustify(self, words, maxWidth):
        
        if not words:
            return []
            
        sum_len = len(words[0])
        cur_words = [words[0]]
        res = []
        
        for word in words[1:]:
            sum_len += len(word) + 1
            if sum_len > maxWidth:
                # format curwords as a line

                if len(cur_words) == 1:
                    # just 1 word
                    cur_line = cur_words[0] + " " * (maxWidth - len(cur_words[0]))
                
                else:
                    # more than 1 words
                    total_len = sum(len(w) for w in cur_words)
                    total_n_spaces = maxWidth - total_len
                    n_words = len(cur_words) - 1
                    per_n_spaces = math.ceil(total_n_spaces / n_words)
                    cur_line = cur_words[0]
                    for w in cur_words[1:]:
                        cur_line += " " * per_n_spaces + w
                        total_n_spaces -= per_n_spaces
                        n_words -= 1
                        if n_words != 0 and math.ceil(total_n_spaces / n_words) != per_n_spaces:
                            per_n_spaces = math.ceil(total_n_spaces / n_words)
                            
                res.append(cur_line)

                # refresh
                cur_words = [word]
                sum_len = len(word)
            else:
                cur_words.append(word)
                
        # last line
        last_line = cur_words[0]
        for word in cur_words[1:]:
            last_line += " " + word
        last_line += " " * (maxWidth - len(last_line))
        res.append(last_line)
        
        return res
