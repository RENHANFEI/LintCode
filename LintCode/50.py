class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        if not nums:
            return
        
        product = 1
        ans = []
        
        for num in nums:
            ans.append(product)
            product *= num
        
        print(ans)
        n = len(nums)
        product = 1
        for i, num in enumerate(nums[::-1]):
            ans[n - i - 1] *= product
            product *= num
            
        return ans