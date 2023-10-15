from collections import Counter
import numpy as np
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows,cols = list(map(tuple,grid)), list(map(tuple,np.array(grid).T))
        rows_counter = Counter(rows)
        cols_counter = Counter(cols)
        common = set(rows_counter.keys()) & set(cols_counter.keys())
        res = 0
        for com in common:
            res += rows_counter[com] * cols_counter[com]
        return res