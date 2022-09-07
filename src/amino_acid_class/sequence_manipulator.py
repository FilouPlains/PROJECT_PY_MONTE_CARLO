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
                    break
            # "snail case", restarting the protein placement.
            if not coord_bad:
                break

    def get_sequence(self):
        """Getting of the sequence of the amino acid.

        Returns
        -------
        list of AminoAcid.
            Return a list of amino acid to manipulate them.
        """
        return self.link_sequence
