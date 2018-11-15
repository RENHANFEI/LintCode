# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

from collections import deque

class Solution(object):
    def __init__(self):
        self.queue = deque()
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while True:
            buf4 = [''] * 4
            count = read4(buf4)
            self.queue.extend(buf4)
            count = min(len(self.queue), n - idx)
            if not count:
                return idx
            for i in range(count):
                buf[idx] = self.queue.popleft()
                idx += 1
            
        return idx