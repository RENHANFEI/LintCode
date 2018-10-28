from collections import defaultdict
class Solution:
    """
    @param grid: the grid
    @return: the number of corner rectangles
    """
    def countCornerRectangles(self, grid):
        column_points = defaultdict(lambda: set())
        
        for i, row in enumerate(grid):
            for j, elem in enumerate(row):
                if elem == 1:
                    column_points[j].add(i)
        
        print(column_points)
        ans = 0
        for i in range(len(grid)):
            column_i = column_points[i]
            for j in range(i + 1, len(grid)):
                n = len(column_i & column_points[j])
                ans += n * (n - 1) // 2
                
        return ans
