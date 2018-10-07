class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    
    def trapRainWater(self, heights):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m = len(heights)
        n = len(heights[0]) if m else 0

        peakMap = [[0x7FFFFFFF] * n for _ in range(m)]

        q = []

        for x in range(m):
            for y in range(n):
                if x in (0, m - 1) or y in (0, n - 1):
                    peakMap[x][y] = heights[x][y]
                    q.append((x, y))

        while q:
            x, y = q.pop(0)
            for dx, dy in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                nx, ny = x + dx, y + dy
                if nx <= 0 or nx >= m - 1 or ny <= 0 or ny >= n - 1: continue
                limit = max(peakMap[x][y], heights[nx][ny])
                if peakMap[nx][ny] > limit:
                    peakMap[nx][ny] = limit
                    q.append((nx, ny))

        return sum(peakMap[x][y] - heights[x][y] for x in range(m) for y in range(n))

# class Solution:
#     """
#     @param heights: a matrix of integers
#     @return: an integer
#     """
    
#     def trapRainWater(self, heights):
        
#         result = 0
#         height_dict = dict()
        
#         for i, rows in enumerate(heights):
#             for j, height in enumerate(rows):
#                 if height in height_dict:
#                     height_dict[height].append((i,j))
#                 else:
#                     height_dict[height] = [(i,j)]
        
#         height_dict = sorted(height_dict.items(), key=lambda d:d[0])
        
#         while len(height_dict) > 1:
#             height_positions = height_dict.pop(0)
#             cur_height = height_positions[0]
#             positions = height_positions[1]
#             step = height_dict[0][0] - cur_height
       
#             while positions:
#                 position = positions[0]
#                 area = [0]
#                 valid = [True]
#                 self.dfs(position[0], position[1], cur_height, heights, valid, area, step, positions, height_dict)
#                 if valid[0]:
#                     result += area[0] * step
                    
#         return result
    
#     def dfs(self, i, j, cur_height, heights, valid, area, step, positions, height_dict):
#         if not positions:
#             return
#         if (i, j) not in positions:
#             return
#         if i == 0 or i == len(heights) - 1 or j == 0 or j == len(heights[0]) - 1:
#             valid[0] = False
#         height_dict[0][1].append((i,j))
#         positions.remove((i,j))
#         area[0] += 1
#         self.dfs(i + 1, j, cur_height, heights, valid, area, step, positions, height_dict)
#         self.dfs(i - 1, j, cur_height, heights, valid, area, step, positions, height_dict)
#         self.dfs(i, j + 1, cur_height, heights, valid, area, step, positions, height_dict)
#         self.dfs(i, j - 1, cur_height, heights, valid, area, step, positions, height_dict)