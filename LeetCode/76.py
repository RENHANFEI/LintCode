from collections import Counter

class Solution:
    def minWindow(self, s, t):

        if not s or not t:
            return ""

        t_counter = Counter(t)

        min_window = len(s) + 1, 0, 0
        start, end = 0, 0

        s_counter = Counter()
        covered = 0

        while end < len(s):
            ch_end = s[end]
            if ch_end in t_counter:
                s_counter[ch_end] += 1
                if s_counter[ch_end] == t_counter[ch_end]:
                    covered += 1
                    if covered == len(t_counter):    # get the window
                        while start <= end:
                            ch_start = s[start]
                            start += 1
                            if ch_start in t_counter:
                                s_counter[ch_start] -= 1
                                if s_counter[ch_start] < t_counter[ch_start]:
                                    covered -= 1
                                    break
                        cur_len = end - start + 2
                        if cur_len < min_window[0]:
                            min_window = cur_len, start - 1, end
            end += 1

        return "" if min_window[0] == len(s) + 1 else s[min_window[1]:min_window[2] + 1]

# from collections import defaultdict

# class Solution:
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         t_dict = defaultdict(list)
#         for i, ch in enumerate(t):
#             t_dict[ch].append(i)
        
#         ans = ""
        
#         for start, ch in enumerate(s):
#             if t_dict[ch]:
#                 contains = [False] * len(t)
#                 contains[t_dict[ch][0]] = True
#                 idx = start + 1
#                 while False in contains and idx < len(s):
#                     cur_locs = t_dict[s[idx]]
#                     for loc in cur_locs:
#                         if not contains[loc]:
#                             contains[loc] = True
#                             break
#                     idx += 1
#                 if not (False in contains):
#                     window = s[start:idx]
#                     if ans:
#                         ans = ans if len(ans) < len(window) else window
#                     else:
#                         ans = window
                        
#         return ans

s = "ADOBECODEBANC"
t = "ABC"
sol = Solution()
print(sol.minWindow(s, t))