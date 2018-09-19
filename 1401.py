class Solution:
    """
    @param str: the origin string
    @return: the start and end of every twitch words
    """
    def twitchWords(self, str):
        if str == []:
            return
        
        twitch_positions = []
        
        pre_ch = str[0]
        start_pos = 0
        iter_num = 0
        for i, ch in enumerate(str[1:]):
            if ch == pre_ch:
                iter_num += 1
                # 3 consecutive
                if iter_num == 2:
                    start_pos = i - 1
                # more than 3 consecutive
                # do nothing
            else:
                # end of a consecutive
                if iter_num >= 2:
                    twitch_positions.append([start_pos, i])
                pre_ch = ch
                iter_num = 0
                
        if iter_num >= 2:
            twitch_positions.append([start_pos, i+1])
                
        return twitch_positions