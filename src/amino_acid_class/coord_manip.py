"""Class that represent all amino acids' coordinates into a given sequence.
"""

# Importation of other python module.
import numpy as np


class CoordManip:
    """An object = coordinate of all amino acids in a sequence.
    """

    def __init__(self, seq_size):
        """Constructor of CoordManip.
        """
        # Create a `numpy array` to stock all amino acids coordinates.
        self.coord_list = np.array([[None] * seq_size, [None] * seq_size])

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

    def get_coord_list(self):
        """Getter of coordinates.

        Returns
        -------
        numpy array
            All amino acid's coordinates.
        """
        return self.coord_list
