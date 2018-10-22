class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        
        if not heights:
            return 0
        
        result = 0
        pre_height = 0
        drop_start = False
        
        drop_start_pos = 0
        drop_start_height = 0
        now_store = 0
        
        for i, height in enumerate(heights):
            
            if drop_start:
                if height < drop_start_height:
                    now_store += drop_start_height - height
                else:
                    result += now_store
                    now_store = 0
                    drop_start = False
            else:
                if height < pre_height:
                    drop_start = True
                    drop_start_pos = i - 1
                    drop_start_height = pre_height
                    now_store = pre_height - height
            
            pre_height = height
            
            
        
        if height < drop_start_height:
            re_trav = heights[drop_start_pos:][::-1]
        
            pre_height = 0
            drop_start = False
            
            drop_start_height = 0
            now_store = 0
            
            for height in re_trav:
                if drop_start:
                    if height < drop_start_height:
                        now_store += drop_start_height - height
                    else:
                        result += now_store
                        now_store = 0
                        drop_start = False
                else:
                    if height < pre_height:
                        drop_start = True
                        drop_start_height = pre_height
                        now_store = pre_height - height
                
                pre_height = height
        
            
        return result