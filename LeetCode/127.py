# from collections import defaultdict

# class Solution:
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
#         if endWord not in wordList:
#             return 0
        
#         wordTrans = defaultdict(list)
        
#         for i, w1 in enumerate(wordList):
#             for w2 in wordList[i + 1:]:
#                 diff = 0
#                 acc = True
#                 for k, ch in enumerate(w1):
#                     if ch != w2[k]:
#                         if diff >= 1:
#                             acc = False
#                             break
#                         diff += 1
#                 if acc:
#                     wordTrans[w1].append(w2)
#                     wordTrans[w2].append(w1)
                    
#         visited = set()
#         bfs = []
        
#         for word in wordList:
#             diff = 0
#             acc = True
#             for k, ch in enumerate(word):
#                 if ch != beginWord[k]:
#                     if diff >= 1:
#                         acc = False
#                         break
#                     diff += 1
#             if acc:
#                 bfs.append(word)
#                 visited.add(word)
                    
#         length = 1
        
#         while bfs:
#             length += 1
#             new_bfs = []
#             for word in bfs:
#                 if word == endWord:
#                     return length
#                 for acc_word in wordTrans[word]:
#                     if acc_word not in visited:
#                         new_bfs.append(acc_word)
#                         visited.add(acc_word)
#             bfs = new_bfs
        
#         return 0

# from collections import defaultdict, deque

# class Solution:
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
#         if endWord not in wordList:
#             return 0
        
#         wordList.insert(0, beginWord)
#         wordTrans = defaultdict(set)
        
#         for i, w1 in enumerate(wordList):
#             for w2 in wordList[i + 1:]:
#                 diff = 0
#                 acc = True
#                 for k, ch in enumerate(w1):
#                     if ch != w2[k]:
#                         if diff >= 1:
#                             acc = False
#                             break
#                         diff += 1
#                 if acc:
#                     wordTrans[w1].add(w2)
#                     wordTrans[w2].add(w1)
                    
#         visited = set([beginWord])
#         bfs = deque([(beginWord, 1)])
        
#         while bfs:
#             word, steps = bfs.popleft()
#             if word == endWord:
#                 return steps
#             for w in wordTrans[word]:
#                 if w not in visited:
#                     visited.add(w)
#                     bfs.append((w, steps + 1))
        
#         return 0

from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList.append(beginWord)
        word_dict = self.preprocess(wordList)

        visited = set([beginWord])
        bfs = deque([(beginWord, 1)])

        while bfs:
            word, steps = bfs.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                key = word[:i] + '_' + word[i + 1:]
                acc_words = word_dict[key]
                for acc_word in acc_words:
                    if acc_word not in visited:
                        visited.add(acc_word)
                        bfs.append((acc_word, steps + 1))

        return 0

    def preprocess(self, wordList):
        word_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '_' + word[i + 1:]
                word_dict[key].append(word)

        return word_dict

sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

print(sol.ladderLength(beginWord, endWord, wordList))
