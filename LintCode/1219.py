class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        ans = 0
        idx_heater = 0
        num_heater = len(heaters)
        
        houses.sort()
        heaters.sort()
        
        for house in houses:
            
            while idx_heater < num_heater - 1 and heaters[idx_heater + 1] < house:
                idx_heater += 1
            
            if idx_heater < num_heater - 1:
                min_radius = min(abs(house - heaters[idx_heater]), 
                        heaters[idx_heater + 1] - house)
            else:
                min_radius = abs(house - heaters[idx_heater])
                
            ans = max(ans, min_radius)
            
        return ans


# class Solution:
#     """
#     @param houses: positions of houses
#     @param heaters: positions of heaters
#     @return: the minimum radius standard of heaters
#     """
#     def findRadius(self, houses, heaters):
#         ans = 0
#         idx_heater = 0
#         num_heater = len(heaters)
        
#         houses.sort()
#         heaters.sort()
        
#         for house in houses:
#             min_radius = house - heaters[idx_heater]
#             flag = False
#             while idx_heater < num_heater and heaters[idx_heater] < house:
#                 min_radius = house - heaters[idx_heater]
#                 idx_heater += 1
#                 flag = True
#             if idx_heater < num_heater:
#                 min_radius = min(min_radius, heaters[idx_heater] - house)
#             if flag:
#                 idx_heater -= 1
#             ans = max(ans, min_radius)
            
#         return ans