class Solution:
    """
    @param ratings: Children's ratings
    @return: the minimum candies you must give
    """
    def candy(self, ratings):
        if not ratings:
            return 0
        
        pre_rating = ratings[0]
        now_candy = 1
        left2right_candies = [now_candy]
        
        for rating in ratings[1:]:
            if rating > pre_rating:
                now_candy += 1
                left2right_candies.append(now_candy)
            else:
                now_candy = 1
                left2right_candies.append(now_candy)
            pre_rating = rating
        
        pre_rating = ratings[-1]
        now_candy = 1
        right2left_candies = [now_candy]
        for rating in ratings[:-1][::-1]:
            if rating > pre_rating:
                now_candy += 1
                right2left_candies.append(now_candy)
            else:
                now_candy = 1
                right2left_candies.append(now_candy)
            pre_rating = rating
        
        candies = [max(left2right_candies[i], right2left_candies[-i-1]) 
                for i in range(len(ratings))]
        
        return sum(candies)
            

# class Solution:
#     """
#     @param ratings: Children's ratings
#     @return: the minimum candies you must give
#     """
#     def candy(self, ratings):
#         if not ratings:
#             return 0
            
#         if len(ratings) == 1:
#             return 1
        
#         pre_rating = ratings[0]
#         now_candy = 1
#         ans = now_candy
#         increasing = 1 if ratings[1] > pre_rating else -1
#         top = 0
#         now_top = 0
        
#         for rating in ratings[1:]:
#             if increasing * rating > increasing * pre_rating:
#                 now_candy += 1
#                 now_top = now_candy
#                 ans += now_candy
#             elif rating == pre_rating:
#                 now_candy = 1
#                 ans += now_candy
#                 now_top = now_candy
#             else:
#                 if increasing < 0:
#                     if now_top >= top and top != 0:
#                         ans += now_top - top + 1
#                     now_top = now_candy = 2
#                 else:
#                     top = now_top
#                     now_top = now_candy = 1
#                 ans += now_candy
#                 increasing = -increasing
#             pre_rating = rating
#             print(ans)
        
#         print((increasing, now_top, top))
#         if increasing < 0 and now_top >= top and top != 0:
#             ans += now_top - top + 1
            
#         return ans
