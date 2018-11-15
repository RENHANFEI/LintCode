import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k_large = nums[:k]
        heapq.heapify(k_large)
        
        for num in nums[k:]:
            if num > k_large[0]:
                heapq.heapreplace(k_large, num)
                
        return k_large[0]