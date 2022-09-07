import numpy as np

class CoordManip:
    def __init__(self, seq_size):
        self.coord_list = np.array([[None] * seq_size, [None] * seq_size])
        
    def is_coord_use(self, coord):
        x = coord[0]
        y = coord[1]
        
        return y in self.coord_list[1, self.coord_list[0] == x]
