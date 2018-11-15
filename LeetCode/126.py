from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList.append(beginWord)
        words_dict = self.preprocess(wordList)

        bfs = deque([([beginWord], {beginWord})])

        length = 0
        ans = []

        while bfs:
            path, visited = bfs.popleft()
            if length > 0 and len(path) >= length:
                continue
            word = path[-1]
            for i in range(len(word)):
                key = word[:i] + '_' + word[i + 1:]
                acc_words = words_dict[key]
                for acc_word in acc_words:
                    if acc_word not in visited:
                        new_path = path + [acc_word]
                        new_visited = visited | {acc_word}
                        if acc_word == endWord:
                            ans.append(new_path)
                            length = len(new_path)
                        else:
                            bfs.append((new_path, new_visited))
                    
        return ans
        
    def preprocess(self, wordList):
        words_dict = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '_' + word[i + 1:]
                words_dict[key].append(word)
                
        return words_dict


sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log", "cog"]
# sol.findLadders(beginWord, endWord, wordList)
print(sol.findLadders(beginWord, endWord, wordList))