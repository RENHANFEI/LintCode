class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        i = 0
        while seats[i] == 0:
            i += 1
        
        max_distance = i
        last_seated = i
        while i < len(seats):
            if seats[i]: 
                max_distance = max(max_distance, (i - last_seated) // 2)
                last_seated = i
            i += 1

        max_distance = max(max_distance, i - last_seated - 1)

        return max_distance

