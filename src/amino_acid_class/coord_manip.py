import numpy as np


class CoordManip:
    def __init__(self, seq_size):
        self.coord_list = np.array([[None] * seq_size, [None] * seq_size])

    def is_coord_use(self, coord):
        x = coord[0]
        y = coord[1]
        
        return y in self.coord_list[1, self.coord_list[0] == x]

    def set_coord(self, id, x, y):
        self.coord_list[0, id] = x
        self.coord_list[1, id] = y

    def __str__(self):
        return f"Coords are:\n{self.coord_list}"