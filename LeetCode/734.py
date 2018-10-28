from collections import defaultdict

class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        # key: a word, value: a set of similar words
        similar_dict = defaultdict(lambda: set())
        for w1, w2 in pairs:
            similar_dict[w1].add(w2)
            similar_dict[w2].add(w1)

        for i, w1 in enumerate(words1):
            w2 = words2[i]
            if w2 == w1: continue
            if w2 not in similar_dict[w1]: return False

        return True

words1 = ["great","acting","skills"]
words2 = ["fine","drama","talent"]
pairs = [["great","fine"],["drama","acting"],["skills","talent"]]

sol = Solution()

print(sol.areSentencesSimilar(words1, words2, pairs))