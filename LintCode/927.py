class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, S):
        words = S.split(" ")
        return " ".join(words[::-1])


# class Solution:
#     """
#     @param str: a string
#     @return: return a string
#     """
#     def reverseWords(self, S):
#         S = list(S)
#         S = S[::-1] + [" "]
        
#         i = 0
#         for j, ch in enumerate(S):
#             if ch == " ":
#                 S[i:j] = S[i:j][::-1]
#                 i = j + 1
        
#         return "".join(S[:-1])
