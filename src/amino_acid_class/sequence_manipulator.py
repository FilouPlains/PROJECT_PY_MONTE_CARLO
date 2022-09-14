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

    # Constant for square root of 2.
    SQRT_2 = 2 ** (1 / 2)

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
        """Return a list of all actual amino acid H/P model.

        Returns
        -------
        list of string
            List of H/P model based on each amino acid in this actual sequence.
        """
        model_list = []

        for amino_acid in self.link_sequence:
            model_list += [amino_acid.get_model()]

        return model_list

    def get_seq_length(self):
        """Getter of the sequence's length.

        Returns
        -------
        int
            The sequence's length.
        """
        return len(self.link_sequence)

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
        if amino_acid.get_neigh()[0] is not None and \
                amino_acid.get_neigh()[1] is not None:
            return False

        move_list = [-1, 1]
        shuffle(move_list)

        which_axe = [True, False]
        shuffle(which_axe)

        if amino_acid.get_neigh()[0] is not None:
            id = amino_acid.get_neigh()[0].get_id()
        else:
            id = amino_acid.get_neigh()[1].get_id()

        print("test2", type(self.coord_manip.get_coord_list()))
        print(np.shape(self.coord_manip.get_coord_list))
        print("test2", self.coord_manip.get_coord_list())

        print(self.coord_manip.get_coord_list()[0])

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
        elif amino_acid.get_neigh()[0] is None or \
                amino_acid.get_neigh()[1] is None:
            return False

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

        if dist == self.SQRT_2:
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

    def crankshaft_move(self, amino_acid, do_shift=True):
        """Try to effectuate a crankshaft move. If all conditions are met, do
        it.

        Parameters
        ----------
        amino_acid : AminoAcid
            The amino acid to be moved.
        do_shift : bool
            If `True`, call on recursion with amino acid's left neighbour as the
            new neighbour. Else, if `False`, do none of that.

        Returns
        -------
        bool
            `True` if placement succeed, else `False`.
        """
        # Return `False` when the sequence is less than 4 amino acids.
        if len(self.link_sequence) < 4:
            return False
        # Return `False` when the amino acid is at end chain.
        elif amino_acid.get_neigh()[0] is None or \
                amino_acid.get_neigh()[1] is None:
            return False
        # If left and right amino acids of this moved amino acid both do not
        # have a neighbour, return `False`.
        elif amino_acid.get_neigh()[0].get_neigh()[0] is None \
                and amino_acid.get_neigh()[1].get_neigh()[1] is None:
            return False

        # Try first case : get 2 left neighbors and 1 right.
        if amino_acid.get_neigh()[0].get_neigh()[0] is not None:
            # Define all neighbors and coordinates.
            left_neigh = amino_acid.get_neigh()[0]
            left_x = self.coord_manip.get_coord_list()[0, left_neigh.get_id()]
            left_y = self.coord_manip.get_coord_list()[1, left_neigh.get_id()]

            way_neigh = amino_acid.get_neigh()[0].get_neigh()[0]
            way_x = self.coord_manip.get_coord_list()[0, way_neigh.get_id()]
            way_y = self.coord_manip.get_coord_list()[1, way_neigh.get_id()]

            right_neigh = amino_acid.get_neigh()[1]
            right_x = self.coord_manip.get_coord_list()[
                0, right_neigh.get_id()]
            right_y = self.coord_manip.get_coord_list()[
                1, right_neigh.get_id()]

            # Define coords of this amino acid.
            id = amino_acid.get_id()
            x = self.coord_manip.get_coord_list()[0, id]
            y = self.coord_manip.get_coord_list()[1, id]

            # Calculate distance.
            bottom_line = ((way_x - right_x) ** 2 + (way_y - right_y) ** 2) \
                ** (1 / 2)

            # Which way to move with the crankshaft.
            if bottom_line == 1:
                if x == right_x:
                    shift_x = 0
                    shift_y = (y - right_y) * 2
                else:
                    shift_x = (x - right_x) * 2
                    shift_y = 0

                # Test if the movement is available.
                coord_bad = self.coord_manip.is_coord_use([x - shift_x,
                                                           y - shift_y])
                coord_bad |= self.coord_manip.is_coord_use([left_x - shift_x,
                                                           left_y - shift_y])

                # If there is not collision between two amino acid validate the
                # placement.
                if not coord_bad:
                    self.coord_manip.set_coord(id, x - shift_x, y - shift_y)
                    self.coord_manip.set_coord(
                        left_neigh.get_id(),
                        left_x - shift_x,
                        left_y - shift_y
                    )

                    return True
            # Next step are for shifting from actual to right amino acid.
            elif do_shift:
                self.crankshaft_move(amino_acid.get_neigh()[1], False)
        elif do_shift:
            self.crankshaft_move(amino_acid.get_neigh()[1], False)

        return False
