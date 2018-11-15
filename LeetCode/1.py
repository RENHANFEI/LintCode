class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        num_position = dict()
        
        for i, num in enumerate(nums):
            if num in num_position:
                num_position[num].append(i)
            else:
                num_position[num] = [i]
        
        for num, positions in num_position.items():
            for position in positions:
                if target - num in num_position:
                    candidates = num_position[target - num]
                    for candidate in candidates:
                        if candidate != position:
                            return position, candidate
        