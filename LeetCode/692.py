from collections import Counter
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = Counter()
        
        for word in words:
            counter[word] += 1
        
        return sorted(list(counter), key=lambda x: (-counter[x], x))[:k]
        
        
        