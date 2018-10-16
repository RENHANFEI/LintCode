class Solution:
    """
    @param nums: an array of integers
    @param k: an integer
    @return: the number of unique k-diff pairs
    """
    def findPairs(self, nums, k):
        
        ans = 0
        num_set = set(nums)
        
        if k == 0:
            num_dict = dict([(num, 0) for num in num_set])
            for num in nums:
                num_dict[num] += 1
            for num, times in num_dict.items():
                if times > 1:
                    ans += 1
        
        else:
            possible_nums = set()
            
            for num in num_set:
                possible_nums.add(num + k)
                possible_nums.add(num - k)
                if num in possible_nums:
                    ans += 1
                
        return ans
