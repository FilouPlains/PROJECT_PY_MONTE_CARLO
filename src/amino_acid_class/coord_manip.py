"""Class that represent all amino acids' coordinates into a given sequence.
"""

# Importation of other python module.
from copy import deepcopy

import numpy as np


class CoordManip:
    """An object = coordinate of all amino acids in a sequence.
    """

    def __init__(self, seq_size):
        """Constructor of CoordManip.

        Parameters
        ----------
        seq_size : int
            The size of a sequence.
        """
        # Create a `numpy array` to stock all amino acids coordinates.
        self.coord_list = np.array([np.full(seq_size, None),
                                    np.full(seq_size, None)])

        # Instantiate his futur copy
        self.copy_coord_list = None

    def __str__(self):
        """Using `print()` while have a personalize message.

        Returns
        -------
        string
            Return a string to display with `print()` the array of coordinates.
        """
        return f"Coords are:\n{self.coord_list}"

    def is_coord_use(self, coord):
        """Check if the given coordinate are not already "used" by an amino
           acid.

        Parameters
        ----------
        coord : list of int
            The coordinates to test.

        Returns
        -------
        bool
            `True` if the coordinate already used. `False` if there's no amino
            acid in the given coordinates.
        """
        x = coord[0]
        y = coord[1]

        return y in self.coord_list[1, self.coord_list[0] == x]

    def set_coord(self, id, x, y):
        """Setter of the coordinate of ONE amino acid.

        Parameters
        ----------
        id : int
            Position of the amino acid into the sequence.
        x : int
            X position.
        y : int
            Y position.
        """
        self.coord_list[0, id] = x
        self.coord_list[1, id] = y

    def set_whole_coord(self, buffer):
        """Reset coordinates after doing an unfavourable move in Monte Carlo.

        Parameters
        ----------
        buffer : np.array(np.array(int), np.array(int))
            All coordinates
        """
        self.coord_list = np.asarray(deepcopy(buffer))

    def get_coord_list(self):
        """Getter of coordinates.

        Returns
        -------
        numpy array
            All amino acid's coordinates.
        """
        return np.asarray(self.coord_list)

    def reset_placement(self):
        """Reset all (x, y) amino acids' coord.
        """
        # Reset the `numpy array` with `None` value.
        self.coord_list = np.full(self.coord_list.shape, None)

    def calc_energy(self, model):
        """Calculate protein energy.

        Parameters
        ----------
        model : list[string]
            List of model H/P of this sequence.

        Returns
        -------
        float
            The energy of the sequence after calculation.
        """
        energy = 0
        is_h = False
        model = np.asarray(model)

        for i in range(len(model)):
            if model[i] == "H":
                x = self.get_coord_list()[0, i]
                y = self.get_coord_list()[1, i]

                filter = np.isin(self.coord_list[0], x + np.array([-1, 1])) \
                    & np.isin(self.coord_list[1], y)
                filter |= np.isin(self.coord_list[0], x) \
                    & np.isin(self.coord_list[1], y + np.array([-1, 1]))
                filter &= (model == "H")

                energy += np.sum(filter) * -0.5
                
                if is_h:
                    energy += 1

                is_h = True
            else:
                is_h = False

        return energy
