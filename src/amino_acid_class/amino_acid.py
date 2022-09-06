class AminoAcid:
    # Redefinition of classical method/operator.
    def __init__(self, model):
        self.model = model
        self.x = None
        self.y = None
    
    def __str__(self):
        return (f"Amino acid class into '{self.model}'. With x = {self.x} and y"
                f" = {self.y}")

    # Setting neighbors.
    def left_neigh(self, neighbour):
        self.left = neighbour

    def right_neigh(self, neighbour):
        self.right = neighbour

    # Setting coords.
    def set_coord(self, coord):
        if self.check_overlap(coord[0], coord[1], True) and \
        self.check_overlap(coord[0], coord[1], False):
            self.x, self.y = coord
            return True
        else:
            return False
    
    def set_x(self, x):
        return self.set_coord((x, self.y))

    def set_y(self, y):
        return self.set_coord((self.x, y))

    # Getting coords.
    def get_coord(self):
        return (self.x, self)

    def get_x(self):
        return self.get_coord[0]

    def get_y(self):
        return self.get_coord[1]

    # Checking overlap.
    def check_overlap(self, x, y, left=True):
        if left:
            if self.left == None:
                return True
            elif x == self.x and y == self.y:
                return False
            else:
                return True and self.left.check_overlap(x, y)
        else:
            if self.right == None:
                return True
            elif x == self.x and y == self.y:
                return False
            else:
                return True and self.right.check_overlap(False, x, y)

