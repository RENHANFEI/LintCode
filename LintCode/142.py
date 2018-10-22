class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        if n <= 0:
            return False
            
        cnt = 0
        while 1:
            if n == 0:
                return True
            if n & 1!= 0:
                if cnt >= 1:
                    return False
                cnt += 1
                n = n >> 1
            else:
                n = n >> 1