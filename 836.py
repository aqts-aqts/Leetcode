from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rec1_left = rec1[0]
        rec1_bottom = rec1[1]
        rec1_right = rec1[2]
        rec1_top = rec1[3]
        
        rec2_left = rec2[0]
        rec2_bottom = rec2[1]
        rec2_right = rec2[2]
        rec2_top = rec2[3]
        
        left_x_max = max(rec1_left, rec2_left)
        right_x_min = min(rec1_right, rec2_right)
        
        bottom_y_max = max(rec1_bottom, rec2_bottom)
        top_y_min = min(rec1_top, rec2_top)
        
        if right_x_min - left_x_max <= 0 or top_y_min - bottom_y_max <= 0:
            return False
        return True