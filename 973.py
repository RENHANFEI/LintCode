class Solution:
    """
    @param bits: a array represented by several bits. 
    @return: whether the last character must be a one-bit character or not
    """
    def isOneBitCharacter(self, bits):
        
        if len(bits) == 1:
            return True
        
        while len(bits) > 2:
            if bits[0] == 1:
                bits = bits[2:]
            else:
                bits = bits[1:]
                
        if bits[0] == 1:
            return False
        else:
            return True