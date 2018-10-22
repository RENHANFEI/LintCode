class Solution:
    """
    @param A: A positive integer which has N digits, A is a string
    @param k: Remove k digits
    @return: A string
    """
    def DeleteDigits(self, A, k):
        if k == len(A):
            return 0
            
        A_list = list(A)
        
        i = 0
        N = len(A)
        while k > 0 and i < N - 1:
            flag = True
            for i in range(len(A_list) - 1):
                if A_list[i] > A_list[i + 1]:
                    A_list.pop(i)
                    flag = False
                    break
            if flag:
                A_list.pop()
            k -= 1
            
        ans = ''.join(A_list)
        
        while ans[0] == '0':
            ans = ans[1:]
            if not ans:
                return 0
            
        return ans