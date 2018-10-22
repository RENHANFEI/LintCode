from collections import deque

class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        word = []
        words = deque()
        
        for ch in s:
            if ch != ' ':
                word += ch
            else:
                if word:
                    words.appendleft(''.join(word))
                    word = []
                
        words.appendleft(''.join(word))
            
        return ' '.join(words)

# class Solution:
#     """
#     @param: s: A string
#     @return: A string
#     """
#     def reverseWords(self, s):
#         return " ".join(filter(lambda a:a!="", s.split(' ')[::-1]))