# Importation of other python module.
from random import shuffle

# Importation of "homemade" python module.
import amino_acid_class.amino_acid as aa
import amino_acid_class.coord_manip as co_manip


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

            link_sequence[i].set_id(i)

        link_sequence[i].right_neigh(None)

        self.link_sequence = link_sequence
        self.coord_manip = co_manip.CoordManip(len(sequence))

    def set_path(self, is_linear=True):
        if is_linear:
            self.__set_linear()
        else:
            self.__set_random()

    def __set_linear(self):
        y = 0

        for amino_acid in self.link_sequence:
            id = amino_acid.get_id()
            self.coord_manip.set_coord(id, 0, y)

            y += 1

        print(self.coord_manip)

    def __set_random(self):
        x = 0
        y = 0

        self.coord_manip.set_coord(0, x, y)
        seq_well_set = False

        while not seq_well_set:
            for amino_acid in self.link_sequence[1:]:
                move_list = [-1, 1]
                shuffle(move_list)

                which_axe = [True, False]
                shuffle(which_axe)

                coord_good = False

                for move in move_list:
                    for select_x in which_axe:
                        # print(amino_acid)

                        if select_x:
                            shift_x = x + move
                            shift_y = y
                        else:
                            shift_x = x
                            shift_y = y + move
                            
                        coord_bad = self.coord_manip.is_coord_use([shift_x,
                                                                    shift_y])
                        
                        if not coord_bad:
                            id = amino_acid.get_id()
                            self.coord_manip.set_coord(id, shift_x, shift_y)

                            x = shift_x
                            y = shift_y
                            
                            break
                    if not coord_bad:
                        break
                if coord_bad:
                    break
            if not coord_bad:
                break
            

    def get_sequence(self):
        return self.link_sequence
