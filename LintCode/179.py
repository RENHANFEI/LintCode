class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param i: A bit position
    @param j: A bit position
    @return: An integer
    """
    def updateBits(self, n, m, i, j):
        
        a = []
        for k in range(32):
            a.append(n % 2)
            n //= 2

        for k in range(i, j + 1):
            a[k] = m % 2
            m //= 2

        n = 0
        for k in range(31):
            if a[k] == 1:
                n |= (1 << k)
        if a[31] == 1:
            n -= 1 << 31
        return n
