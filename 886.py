class Solution:
    """
    @param point: a list of two-tuples
    @return: a boolean, denote whether the polygon is convex
    """
    def isConvex(self, points):
        points.append(points[0])
        points.append(points[1])
        
        pre_edge = [points[1][0] - points[0][0], points[1][1] - points[0][1]]
        
        positive_flag = False
        negative_flag = False
        
        for i in range(len(points) - 2):
            edge = [points[i+2][0] - points[i+1][0], points[i+2][1] - points[i+1][1]]
            cp = self.crossProduct(pre_edge, edge)
            if cp == 1:
                positive_flag = True
            elif cp == -1:
                negative_flag = True
                
            pre_edge = [edge[0], edge[1]]
                
        if positive_flag != negative_flag:
            return True
        else:
            return False
            
    
    def crossProduct(self, pre_edge, edge):
        cp = pre_edge[0] * edge[1] - pre_edge[1] * edge[0]
        if cp > 0:
            return 1
        elif cp < 0:
            return -1
        else:
            return 0