class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    
    
    def findShortestSubArray(self, nums):
        
        num_times = dict()
        max_degree = 0
        ans = 0
        
        for i, num in enumerate(nums):
            if num in num_times:
                num_times[num][0] += 1
                num_times[num][2] = i
            else:
                num_stance = [1, i, i]  # times, start_idx, end_idx
                num_times[num] = num_stance
                
            if num_times[num][0] == max_degree:
                ans = min(ans, num_times[num][2] - num_times[num][1] + 1)
            
            if num_times[num][0] > max_degree:
                max_degree = num_times[num][0]
                ans = num_times[num][2] - num_times[num][1] + 1
                
        return ans