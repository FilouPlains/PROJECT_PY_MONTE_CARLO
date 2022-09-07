"""Class that represents the amino acid in a sequence.
"""

class AminoAcid:
    """An object = an amino acid. Know their neighbors, id and the model.
    """
    def __init__(self, model):
        """Constructor of AminoAcid.

        Parameters
        ----------
        model : string
            Which type of model between H or P the new object going to be.
        """
        self.model = model
        # Number in the sequence to access to coordinates.
        self.id = None
        # Neighbour as pointer.
        self.left = None
        self.right = None

    def __str__(self):
        """Using `print()` while have a personalize message.

        Returns
        -------
        string
            Return a string to display with `print()` both main attribute, which
            are `model` and `id`.
        """
        return f"Amino acid class into '{self.model}'. With ID.{self.id}"

    # Setting neighbors.
    def left_neigh(self, neighbour):
        """Setting the left neighbour of this amino acid object.

        Parameters
        ----------
        neighbour : AminoAcid
            The left neighbour of this amino acid object.
        """
        self.left = neighbour

    def right_neigh(self, neighbour):
        """Setting the right neighbour of this amino acid object.

        Parameters
        ----------
        neighbour : AminoAcid
            The right neighbour of this amino acid object.
        """
        self.right = neighbour

    # Getter and setter of id.
    def set_id(self, id):
        """Set the id of this amino acid object.

        Parameters
        ----------
        id : int
            The id of this amino acid object.
        """
        self.id = id

    def get_id(self):
        """Get the id of this amino acid object.

        Returns
        -------
        int
            The id of this amino acid object.
        """
        return self.id
