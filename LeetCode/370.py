from collections import Counter

class Solution:
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        update_counter = Counter()
        for start, end, inc in updates:
            update_counter[start] += inc
            update_counter[end + 1] -= inc

        ans = []
        val = 0
        for i in range(length):
            val += update_counter[i]
            ans.append(val)

        return ans

# class Solution:
#     def getModifiedArray(self, length, updates):
#         """
#         :type length: int
#         :type updates: List[List[int]]
#         :rtype: List[int]
#         """
#         array = [0] * length
#         for update in updates:
#             start, end, inc = update[0], update[1], update[2]
#             for i in range(start, end + 1):
#                 array[i] += inc

#         return array

