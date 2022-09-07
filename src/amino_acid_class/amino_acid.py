class AminoAcid:
    # Redefinition of classical method/operator.
    def __init__(self, model):
        self.model = model
        self.id = None

    def __str__(self):
        return (f"Amino acid class into '{self.model}'. With ID.{self.id}")

    # Setting neighbors.
    def left_neigh(self, neighbour):
        self.left = neighbour

    def right_neigh(self, neighbour):
        self.right = neighbour

    def set_id(self, id):
        self.id = id
        
    def get_id(self):
        return self.id
