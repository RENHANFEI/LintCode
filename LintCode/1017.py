class Solution:
    """
    @param color: the given color
    @return: a 7 character color that is most similar to the given color
    """
    def similarRGB(self, color):
        return "#" + self.similarChannel(color[1:3]) + \
            self.similarChannel(color[3:5]) + self.similarChannel(color[5:])
        
    
    def similarChannel(self, c):
        # channel is a 2-char string
        c_dec = int(c, 16)
        candidate = int(c[0] + c[0], 16) # a possibility
        difference = candidate - c_dec
        if difference <= 0x9 and difference > -0x9:
            return hex(candidate)[2:] if candidate != 0x0 else "00"
        elif difference > 0x9:
            return hex(candidate - 0x11)[2:] if (candidate != 0x0 and candidate - 0x11 != 0x0) else "00"
        else:
            return hex(candidate + 0x11)[2:]


s = Solution()

a = "#0f166"
print(s.similarRGB(a))


