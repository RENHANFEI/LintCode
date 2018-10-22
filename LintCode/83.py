class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumberII(self, A):
        aa_dict = dict()
        for a in A:
            if a in aa_dict:
                if aa_dict[a] == 2:
                    aa_dict.pop(a)
                else:
                    aa_dict[a] += 1
            else:
                aa_dict[a] = 1
                
        return list(aa_dict)[0]
