# Importation of other python module.
from random import shuffle

# Importation of "homemade" python module.
import amino_acid_class.amino_acid as aa

class AminoAcidManip:
    def __init__(self, sequence):
        link_sequence = []
        
        for i in range(len(sequence)):
            if i <= 0:
                link_sequence += [aa.AminoAcid(sequence[i])]
                link_sequence[0].left_neigh(None)
            else:
                link_sequence += [aa.AminoAcid(sequence[i])]
                
                link_sequence[i].left_neigh(link_sequence[i - 1])
                link_sequence[i - 1].right_neigh(link_sequence[i])
        
        link_sequence[i].right_neigh(None)

        self.link_sequence = link_sequence
        
    def set_path(self, is_linear=True):
        if is_linear:
            self.__set_linear()
        else:
            self.__set_random()
    
    def __set_linear(self):
        y = 0
        
        for amino_acid in self.link_sequence:
            amino_acid.set_coord((0, y))
            
            y += 1

    def __set_random(self) :
        sequence_set = False
        x = 0
        y = 0
        
        self.link_sequence[0].set_coord((x, y))
        
        while not sequence_set:
            for amino_acid in self.link_sequence[1:]:
                valid_coord = False
                move = [-1, 1]
                shuffle(move)
                select_x = [True, False]
                shuffle(select_x)
                
                switch_i = 0
                switch_j = 1
                
                while not valid_coord:
                    if select_x[switch_i]:                
                        new_x = x + move[switch_j >= 3]
                        new_y = y
                    else:
                        new_x = x
                        new_y = y + move[switch_j >= 3]
                    
                    valid_coord = amino_acid.set_coord((new_x, new_y))
                    
                    switch_i = 1 - switch_i
                    switch_j += 1
                    
                    if switch_j > 4:
                        print("WARNING: Conformation could not be fully"
                              " generated. The program will restart the\n"
                              "generation, please wait.")
                        break

                x = new_x
                y = new_y
                
            if switch_j <= 4:
                sequence_set = True
                

    def get_sequence (self):
        return self.link_sequence
