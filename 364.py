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
        
        height_dict = sorted(height_dict.items(), key=lambda d:d[0])
        
        for i, height_positions in enumerate(height_dict[:-1]):
            cur_height = height_positions[0]
            postions = height_positions[1]
            step = height_positions[i+1][0] - cur_height
            
            valid = [True]
            print(positions)
            while positions:
                positon = positions[0]
                area = self.dfs(position[0], position[1], positions, valid)
                break
            
                    
        return result
    
    def dfs(self, i, j, positions):
        pass
        
