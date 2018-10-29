class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        if not k:
            return []
        
        start, end = 0, len(A) - 1
        ans = []
        
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                ans.append(A[mid])
                i, j = mid - 1, mid + 1
                break
                
        if not ans:
            if target - A[start] <= A[end] - target:
                ans.append(A[start])
                i, j = start - 1, start + 1
            else:
                ans.append(A[end])
                i, j = end - 1, end + 1
                
        while len(ans) < k and i >= 0 and j < len(A):
            if target - A[i] <= A[j] - target:
                ans.append(A[i])
                i -= 1
            else:
                ans.append(A[j])
                j += 1
                
        while len(ans) < k and i >= 0:
            ans.append(A[i])
            i -= 1
            
        while len(ans) < k and j < len(A):
            ans.append(A[j])
            j += 1
                
        return ans
