from collections import defaultdict
class Solution:
    def maxProduct(self, words):
        mask_map = defaultdict(int)
        bit_number = lambda x: ord(x) - ord('a')
        for word in words:
            bit_mask = 0
            for each in word:
                bit_mask |= 1 << bit_number(each)
            mask_map[bit_mask] = max(len(word), mask_map[bit_mask])
        res = 0
        for mask1 in mask_map:
            for mask2 in mask_map:
                if mask1 & mask2 == 0:
                    res = max(res, mask_map[mask1]*mask_map[mask2])
        return res