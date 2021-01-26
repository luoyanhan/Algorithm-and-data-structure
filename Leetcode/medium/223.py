class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int):
        first_left_down = (A, B)
        first_right_top = (C, D)
        sec_left_down = (E, F)
        sec_right_top = (G, H)
        if E < A:
            tmp = first_left_down
            first_left_down = sec_left_down
            sec_left_down = tmp
            tmp = first_right_top
            first_right_top = sec_right_top
            sec_right_top = tmp
        if sec_left_down[0] >= first_right_top[0] or sec_right_top[1] <= first_left_down[1] or \
                sec_left_down[1] >= first_right_top[1]:
            return (first_right_top[0] - first_left_down[0])*(first_right_top[1] - first_left_down[1]) + \
                   (sec_right_top[0] - sec_left_down[0])*(sec_right_top[1] - sec_left_down[1])
        top = min(first_right_top[1], sec_right_top[1])
        down = max(first_left_down[1], sec_left_down[1])
        left = max(first_left_down[0], sec_left_down[0])
        right = min(first_right_top[0], sec_right_top[0])
        return (first_right_top[0] - first_left_down[0])*(first_right_top[1] - first_left_down[1]) + \
                   (sec_right_top[0] - sec_left_down[0])*(sec_right_top[1] - sec_left_down[1]) - \
               abs(top-down)*abs(right-left)
