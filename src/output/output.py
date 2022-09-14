"""This Class manipulate the output file.
"""

class Output():
    """An object = file writer.
    """

    def __init__(self, file, do_mol=False):
        """Constructor to initialize the output file writing.

        Parameters
        ----------
        file : str
            The file to write in.
        do_mol : bool, optional
            If `True`, write a `.mol2`. Else, if `False` write a `.csv` file.
            By default False.
        """
        # Initialize the `.csv` file.
        if not do_mol:
            self.writer = open(file, "w", encoding="utf-8")
            self.writer.write("TEMPERATURE,ENERGY,STEP\n")
        # Initialize the `.mol2` file.
        else:
            self.writer = open(file, "w", encoding="utf-8")

    def add_line(self, temperature, energy, step):
        """Write a ligne in the `.csv` file.

        Parameters
        ----------
        temperature : int
            The replica temperature.
        energy : int
            The actual conformation's energy.
        step : int
            The actual Monte Carlo step.
        """
        self.writer.write(f"{temperature},{energy},{step}\n")

    def end_csv(self):
        """Close the `.csv` file.
        """
        self.writer.close()

    def end_mol2(self):
        """Close the `.mol2` file.
        """
        self.writer.close()

    def write_mol2(self, coord, model):
        """Write a ligne in the `.mol2` file.

        Parameters
        ----------
        coord : numpy.array(numpy.array(), numpy.array())
            Conformation coordinates.
        model : list[str]
            The sequence's H/P model.
        """
        begin = self.__molecule(len(model))
        end = self.__atom_bond(coord, model)

        self.writer.write(begin + end)

    def __molecule(self, nb_atom):
        """Write the `@<TRIPOS>MOLECULE` in the `.mol2` file.

        Parameters
        ----------
        nb_atom : int
            The number of atom in the sequence.

        Returns
        -------
        str
            The line to write about this section.
        """
        molecule = ("@<TRIPOS>MOLECULE\n"
                    "protein_hp_model\n"
                    f"{nb_atom} {nb_atom - 1} 0 0 0\n"
                    "SMALL\n"
                    "NO_CHARGES\n")

        return molecule

    def __atom_bond(self, coord, model):
        """Write the `@<TRIPOS>ATOM` and `@<TRIPOS>BOND` section in the `.mol2`
        file.

        Parameters
        ----------
        coord : numpy.array(numpy.array(), numpy.array())
            Conformation coordinates.
        model : list[str]
            The sequence's H/P model.

        Returns
        -------
        str
            The line to write about this section.
        """
        atom = "@<TRIPOS>ATOM\n"
        bond = "@<TRIPOS>BOND\n"
        length = len(model)
        
        for i in range(len(model)):
            # Define the atom's type for the representation.
            if model[i] == "H":
                type = "C"
            else:
                type = "O"

            # Concatanate the atom's lines section.
            atom += f"{i + 1} {type} {coord[0, i]} {coord[1, i]} 0.000\n"

            # Concatanate the bond's lines section.
            if i < length:
                bond += f"{i + 1} {i + 1} {i + 2} 1\n"

        return atom + bond
