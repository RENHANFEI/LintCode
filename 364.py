class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    def trapRainWater(self, heights):
        
        result = 0
        height_dict = dict()
        
        for i, rows in enumerate(heights):
            for j, height in enumerate(rows):
                if height in height_dict:
                    height_dict[height].append((i,j))
                else:
                    height_dict[height] = [(i,j)]
        
        height_dict = dict(sorted([for item in height_dict.items()], key=item[0]))
        print(height_dict)
                    
        return result
                
