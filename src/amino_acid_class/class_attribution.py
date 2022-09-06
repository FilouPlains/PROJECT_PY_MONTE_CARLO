# Importation of other python module.
from random import shuffle, choice

# Importation of "homemade" python module.
import amino_acid_class.amino_acid as aa

class amino_acid_manip:
    def __init__(self, sequence):
        link_sequence = []
        
        for i in range(len(sequence)):
            if i <= 0:
                link_sequence += [aa.AminoAcid(sequence[i])]
                link_sequence[0].left_neigh(None)
            elif i >= len(sequence):
                link_sequence += [aa.AminoAcid(sequence[i])]
                
                link_sequence[i].left_neigh(link_sequence[i - 1])
                link_sequence[i - 1].right_neigh(link_sequence[i])
            else:
                link_sequence += [aa.AminoAcid(sequence[i])]
                
                link_sequence[i].left_neigh(link_sequence[i - 1])
                link_sequence[i - 1].right_neigh(None)

        self.link_sequence = link_sequence
        
    def set_path(self, is_linear=True):
        if is_linear:
            self.__set_linear()
        else:
            self.__set_random()
    
    def __set_linear(self):
        y = 0
        
        for amino_acid in self.link_sequence:
            amino_acid.set_y(y)
            
            y += 1

    def __set_random(self) :
        sequence_set = False
        x = 0
        y = 0
        
        self.link_sequence[0].set_coord((x, y))
        
        while not sequence_set:
            for amino_acid in self.link_sequence[1:]:
                move = shuffle([-1, 1])
                select_x = choice([True, False])

                if select_x:                
                    new_x = x + move[0]
                    new_y = y
                else:
                    new_x = x
                    new_y = y + move[0]
                
                amino_acid.set_coord((new_x, new_y))

    def get_sequence (self):
        return self.link_sequence
