from collections import defaultdict
class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        if not stones or stones == [0]:
            return True
        
        stone_idx = dict()
        for i, stone in enumerate(stones):
            stone_idx[stone] = i
        
        stone_steps = [set() for _ in stones]
        stone_steps[0].add(0)
        
        step_plus = [-1, 0, 1]
        
        for i, steps in enumerate(stone_steps):
            for step in steps:
                for plus in step_plus:
                    new_step = step + plus
                    if new_step > 0:
                        next_stone = stones[i] + new_step
                        if next_stone in stone_idx:
                            if next_stone == stones[-1]:
                                return True
                            stone_steps[stone_idx[next_stone]].add(new_step)
                            
        return False