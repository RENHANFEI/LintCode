class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        if not houses:
            return 0

        houses.sort()
        heaters.sort()
        
        idx_house = 0
        ans = 0
        
        while idx_house < len(houses) and houses[idx_house] <= heaters[0]:
            ans = max(ans, heaters[0] - houses[idx_house])
            idx_house += 1

        pre_heater = heaters[0]
        post_heater = heaters[1] if len(heaters) > 1 else None
        idx_heater = 0
        house = houses[0]

        while idx_house < len(houses) and houses[idx_house] < heaters[-1]:
            house = houses[idx_house]
            while house > heaters[idx_heater + 1]:
                print(house, heater)
                idx_heater += 1
            pre_heater = heaters[idx_heater]
            pre_distance = house - heaters[idx_heater]
            post_distance = heaters[idx_heater + 1] - house
            ans = max(ans, min(pre_distance, post_distance))
            idx_house += 1
            
        ans = max(ans, houses[-1] - heaters[-1])

        return ans


sol = Solution()
houses = [1,2,3,4]
heaters = [1,4]

houses = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
heaters = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]

print(sol.findRadius(houses, heaters))