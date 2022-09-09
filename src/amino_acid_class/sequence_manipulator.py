"""Class that represent a sequence of given amino acid following H/P model.
"""

# Importation of other python module.
from random import shuffle

# Importation of "homemade" python module.
import amino_acid_class.amino_acid as aa
import amino_acid_class.coord_manip as co_manip


class AminoAcidManip:
    """An object = a sequence and method to manipulate it.
    """

    def __init__(self, sequence):
        """Constructor of AminoAcidManip.

        Parameters
        ----------
        sequence : string
            The sequence in H/P model.
        """
        link_sequence = []

        for i in range(len(sequence)):
            # First amino acid of the sequence.
            if i <= 0:
                link_sequence += [aa.AminoAcid(sequence[i])]
            # All the other one.
            else:
                link_sequence += [aa.AminoAcid(sequence[i])]

                link_sequence[i].left_neigh(link_sequence[i - 1])
                link_sequence[i - 1].right_neigh(link_sequence[i])

            # Set amino acid id == his position in the sequence.
            link_sequence[i].set_id(i)

        # Defining the new list of amino acid == a new sequence.
        self.link_sequence = link_sequence
        # Initialize the object to manipulate coordinates of amino acid.
        self.coord_manip = co_manip.CoordManip(len(sequence))

    def set_path(self, is_linear=True):
        """Setting the sequence into a "grid" to initialize the movement.

        Parameters
        ----------
        is_linear : bool, optional
            If `True`, put the sequence linearly. Else if `False`, set the
            sequence randomly. By default `True`.
        """
        # Set the sequence linearly into a "grid".
        if is_linear:
            self.__set_linear()
        # Set the sequence randomly into a "grid".
        else:
            self.__set_random()

    def __set_linear(self):
        """Set the sequence linearly into a "grid".

        **PRIVATE_METHOD**
        """
        y = 0

        # Simply increase the y from 0 to len(sequence), while maintaining x
        # at 0.
        for amino_acid in self.link_sequence:
            id = amino_acid.get_id()
            self.coord_manip.set_coord(id, 0, y)

            y += 1

    def __set_random(self):
        """Set the sequence randomly into a "grid".

        **PRIVATE_METHOD**
        """
        # Setting the first amino acid to (0, 0).
        x = 0
        y = 0

        self.coord_manip.set_coord(0, x, y)
        seq_well_set = False

        # To prevent a "snail case".
        while not seq_well_set:
            # Parsing trough the string sequence to set amino acid object..
            for amino_acid in self.link_sequence[1:]:
                move_list = [-1, 1]
                shuffle(move_list)

                which_axe = [True, False]
                shuffle(which_axe)

                coord_bad = False

                # Testing all possible directions. If none found, restart the
                # sequence placement.
                for move in move_list:
                    for select_x in which_axe:
                        # Move while following x or y ?
                        if select_x:
                            shift_x = x + move
                            shift_y = y
                        else:
                            shift_x = x
                            shift_y = y + move

                        coord_bad = self.coord_manip.is_coord_use([shift_x,
                                                                   shift_y])

                        # If there is not collision between two amino acid,
                        # validate the placement.
                        if not coord_bad:
                            id = amino_acid.get_id()
                            self.coord_manip.set_coord(id, shift_x, shift_y)

                            x = shift_x
                            y = shift_y

                            break
                    # Both break permit the exit of trying the placement of a
                    # given amino acid when a good one is found.
                    if not coord_bad:
                        break
                if coord_bad:
                    print("'SNAIL CASE', restarting the sequence placement.")

                    x = 0
                    y = 0

                    self.coord_manip.reset_placement()
                    self.coord_manip.set_coord(0, x, y)

                    break
            # "snail case", restarting the protein placement.
            if not coord_bad:
                seq_well_set = True

    def get_link_sequence(self):
        """Getter of the sequence of the amino acid.

        Returns
        -------
        list of AminoAcid
            Return a list of amino acid to manipulate them.
        """
        return self.link_sequence

    def get_coord_manip(self):
        """Getter of the object that threat coordinates for this object.

        Returns
        -------
        CoordManip
            Return the object to manipulate amino acids' coordinates of this
            sequence.
        """
        return self.coord_manip

    def get_sequence_model(self):
        model_list = []

        for amino_acid in self.link_sequence:
            model_list += [amino_acid.get_model()]

        return model_list

    def end_move(self, amino_acid):
        """Try to effectuate a end move. If all conditions are met, do it.

        Parameters
        ----------
        amino_acid : AminoAcid
            The amino acid to be moved.

        Returns
        -------
        bool
            `True` if placement succeed, else `False`.
        """
        # Return `False` when the amino acid is not at end chain.
        if amino_acid.get_neigh()[0] != None and \
                amino_acid.get_neigh()[1] != None:
            return False

        move_list = [-1, 1]
        shuffle(move_list)

        which_axe = [True, False]
        shuffle(which_axe)

        if amino_acid.get_neigh()[0] != None:
            id = amino_acid.get_neigh()[0].get_id()
        else:
            id = amino_acid.get_neigh()[1].get_id()

        x = self.coord_manip.get_coord_list()[0, id]
        y = self.coord_manip.get_coord_list()[1, id]

        # Testing all possible directions. If none found, return `False`.
        for move in move_list:
            for select_x in which_axe:
                # Move while following x or y ?
                if select_x:
                    shift_x = x + move
                    shift_y = y
                else:
                    shift_x = x
                    shift_y = y + move

                coord_bad = self.coord_manip.is_coord_use([shift_x,
                                                           shift_y])

                # If there is not collision between two amino acid,
                # validate the placement.
                if not coord_bad:
                    id = amino_acid.get_id()
                    self.coord_manip.set_coord(id, shift_x, shift_y)

                    return True

        return False

    def corner_move(self, amino_acid):
        """Try to effectuate a corner move. If all conditions are met, do it.

        Parameters
        ----------
        amino_acid : AminoAcid
            The amino acid to be moved.

        Returns
        -------
        bool
            `True` if placement succeed, else `False`.
        """
        # Return `False` when the sequence is less than 4 amino acids.
        if len(self.link_sequence) < 3:
            return False
        # Return `False` when the amino acid is at end chain.
        elif amino_acid.get_neigh()[0] == None or \
                amino_acid.get_neigh()[1] == None:
            return False
        
        # Constant for square root of 2.
        SQRT_2 = 2 ** (1 / 2)

        # Getting neighbors.
        id_neigh = [amino_acid.get_neigh()[0].get_id(),
                    amino_acid.get_neigh()[1].get_id()]

        # Getting coords.
        left_x = self.coord_manip.get_coord_list()[0, id_neigh[0]]
        left_y = self.coord_manip.get_coord_list()[1, id_neigh[0]]

        right_x = self.coord_manip.get_coord_list()[0, id_neigh[1]]
        right_y = self.coord_manip.get_coord_list()[1, id_neigh[1]]

        # Euclidean distance.
        dist = ((left_x - right_x) ** 2 + (left_y - right_y) ** 2) ** (1 / 2)

        if dist == SQRT_2:
            id = amino_acid.get_id()

            x = self.coord_manip.get_coord_list()[0, id]
            y = self.coord_manip.get_coord_list()[1, id]

            # Try to do a corner move. To do so, get x and y from neighbors that
            # are different from the moved amino acid.
            if x == left_x:
                shift_x = right_x
            else:
                shift_x = left_x

            if y == left_y:
                shift_y = right_y
            else:
                shift_y = left_y

            coord_bad = self.coord_manip.is_coord_use([shift_x, shift_y])
            
            # If there is not collision between two amino acid validate the
            # placement.
            if not coord_bad:
                self.coord_manip.set_coord(id, shift_x, shift_y)

                return True

        return False

    def crankshaft_move(self, amino_acid):
        # Return `False` when the sequence is less than 4 amino acids.
        if len(self.link_sequence) < 4:
            return False
        # Return `False` when the amino acid is at end chain.
        elif amino_acid.get_neigh()[0] == None or \
            amino_acid.get_neigh()[1] == None:
            return False
        
        