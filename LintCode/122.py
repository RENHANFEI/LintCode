class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        
        len_histogram = len(height)
        
        ans = 0
        height_list = sorter(height, reverse=True)
        
        for now_height in height_list:
            max_area = 0
            now_area = 0
            for i in range(len_histogram):
                if height[i] >= now_height:
                    now_area += height[i] * now_height
                else:
                    max_area = max(max_area, now_area)
            ans = max(max_area, ans)
            
        return ans
