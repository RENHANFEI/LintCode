class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        diff = [ gas[i] - cost[i] for i in range(len(gas))] * 2
        
        start = 0
        tot = 0
        for i, d in enumerate(diff):
            if i - start >= len(gas):
                return start
            tot += d
            while tot < 0:
                tot -= diff[start]
                start += 1
        
        return -1

# class Solution:
#     """
#     @param gas: An array of integers
#     @param cost: An array of integers
#     @return: An integer
#     """
#     def canCompleteCircuit(self, gas, cost):
        
#         if len(gas) == 1:
#             if cost[0] > gas[0]:
#                 return -1
#             return 1
        
#         for i, g in enumerate(gas):
#             g_store = 0
#             flag = True
#             for j in range(len(cost)):
#                 g_store += gas[(i + j) % len(gas)] - cost[(i + j) % len(cost)]
#                 if g_store < 0:
#                     flag = False
#                     break
#             if flag:
#                 return i
                
#         return -1