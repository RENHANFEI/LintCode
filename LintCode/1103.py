from collections import Counter

class Solution:
    """
    @param nums: a list of integers
    @return: return a boolean
    """
    def isPossible(self, nums):
        left = Counter(nums)    # record nums not placed
        end = Counter()    # record subsequences ended with certain num
        
        for num in nums:
            if not left[num]:
                continue
            
            left[num] -= 1
            
            if end[num - 1]:
                end[num - 1] -= 1
                end[num] += 1
            elif left[num + 1] and left[num + 2]:
                end[num + 2] += 1
                left[num + 1] -= 1
                left[num + 2] -= 1
            else:
                return False
                
        return True
            
