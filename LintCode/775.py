class Solution:
    """
    @param words: a list of unique words
    @return: all pairs of distinct indices
    """
    def palindromePairs(self, words):
        
        result = []
        words_dict = dict([(word, i) for i, word in enumerate(words)])
        
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                # X + word
                if self.isPalindrome(word[:j]) and word[j:][::-1] in words_dict and i != words_dict[word[j:][::-1]]:
                    result.append([words_dict[word[j:][::-1]], i])
                    
                if j == len(word):
                    continue
                    
                # word + X
                if self.isPalindrome(word[j:]) and word[:j][::-1] in words_dict and i != words_dict[word[:j][::-1]]:
                    result.append([i, words_dict[word[:j][::-1]]])
        
        return result
        
        
    def isPalindrome(self, word):
        return word == word[::-1]

# class Solution:
#     """
#     @param words: a list of unique words
#     @return: all pairs of distinct indices
#     """
#     def palindromePairs(self, words):
        
#         res = []
#         words_table = dict()
        
#         for i, word in enumerate(words):
#             words_table[word] = i
        
#         words_table = dict(sorted(words_table.items(), key = lambda w : len(w[0])))
        
#         len_table = dict()
#         for i, w in enumerate(words_table):
#             if len(w) not in len_table:
#                 len_table[len(w)] = i
        
#         for i, word in enumerate(words):
#             if word[::-1] in words_table and words_table[word[::-1]] != i:
#                 res.append([i, words_table[word[::-1]]])
            
#             for k in range(len_table[len(word)]):
#                 w = list(words_table.items())[k][0]
#                 ww = w + word
#                 is_palindrome = True
#                 for k in range((len(ww) + 1) // 2):
#                     if ww[k] != ww[len(ww) - 1 - k]:
#                         is_palindrome = False
#                         break
#                 if is_palindrome:
#                     res.append([words_table[w], i])
                
#                 ww = word + w
#                 is_palindrome = True
#                 for k in range((len(ww) + 1) // 2):
#                     if ww[k] != ww[len(ww) - 1 - k]:
#                         is_palindrome = False
#                         break
#                 if is_palindrome:
#                     res.append([i, words_table[w]])
                    
#         return res
        

# class Solution:
#     """
#     @param words: a list of unique words
#     @return: all pairs of distinct indices
#     """
#     def palindromePairs(self, words):
#         res = []
        
#         for i, w1 in enumerate(words):
#             for j, w2 in enumerate(words[i+1:]):
#                 if w1 and w2 and w1[0] != w2[-1] and w1[-1] != w2[0]:
#                     continue
                
#                 ww = w1 + w2
#                 is_palindrome = True
#                 for k in range((len(ww) + 1) // 2):
#                     if ww[k] != ww[len(ww) - 1 - k]:
#                         is_palindrome = False
#                         break
#                 if is_palindrome:
#                     res.append([i, j + i + 1])
                    
#                 ww = w2 + w1
#                 is_palindrome = True
#                 for k in range((len(ww) + 1) // 2):
#                     if ww[k] != ww[len(ww) - 1 - k]:
#                         is_palindrome = False
#                         break
#                 if is_palindrome:
#                     res.append([j + i + 1, i])
                    
#         return res