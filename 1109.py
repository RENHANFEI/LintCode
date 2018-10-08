class Solution:
    """
    @param senate: a string
    @return: return a string
    """
    def predictPartyVictory(self, senate):
        senators = list(senate)
        parties = {'R':'Radiant', 'D':'Dire'}
        
        i = 0
        while senators:
            if len(set(senators)) == 1:
                return parties[senators[0]]
            
            now = senators[i]
            
            if now == 'R':
                senators.remove('D')
            else:
                senators.remove('R')
            if i >= len(senators) - 1:
                i = 0
            else:
                i += 1
