class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        if not values:
            return False
        if len(values) <= 2:
            return True
        
        dp = {}
        dp[0] = 0 # need dp[0] otherwish infinite loop
        res = self.memo(values, len(values), dp)
        
        return res > sum(values) / 2.0
        
        
        
    def memo(self, values, i, dp):
        if i in dp:
            return dp[i]
        n = len(values)
        
        if i == 1:
            dp[i] = values[-1]
        elif i == 2:
            dp[i] = values[-1] + values[-2]
        elif i == 3:
            dp[i] = values[-3] + values[-2]
        else:
            dp[i] = max(
                min(self.memo(values, i - 2, dp), self.memo(values, i - 3, dp)) + values[n - i], 
                min(self.memo(values, i - 3, dp), self.memo(values, i - 4, dp)) + values[n - i] + values[n - i + 1]
                )
        
        return dp[i]
        

# class Solution:
#     """
#     @param values: a vector of integers
#     @return: a boolean which equals to true if the first player will win
#     """
#     def firstWillWin(self, values):
        
#         dp = [0] * (len(values) + 1)
        
#         first_value = self.firstValue(values, dp)
#         second_value = sum(values) - first_value
        
#         return first_value >= second_value
        
        
#     def firstValue(self, values, dp):
        
#         i = len(values)
        
#         if i in dp:
#             return dp[i]
        
#         if i == 1:
#             dp[i] = values[0]
#             return dp[i]
            
#         if i == 2:
#             dp[i] = values[0] + values[1]
#             return dp[i]
            
#         if i == 3:
#             dp[i] = values[0] + values[1]
#             return dp[i]
            
#         if i == 4:
#             dp[i] = max(values[0] + values[1], values[0] + values[3])
#             return dp[i]
        
#         return max(min(values[0] + self.firstValue(values[2:], dp), values[0] + self.firstValue(values[3:], dp)), min(values[0] + values[1] + self.firstValue(values[4:], dp), values[0] + values[1] + self.firstValue(values[3:], dp)))
        