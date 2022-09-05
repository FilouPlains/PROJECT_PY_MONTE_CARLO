"""Functions necessary for the parsing.
"""

# Importation of other python module.
import argparse

def parsing():
    """This function call the parser to get all necessary program's arguments.

    Returns
    -------
    argparse.ArgumentParser() object
        Permit the accessibility to access to all given arguments with their
        values.
    """
    parser = argparse.ArgumentParser()

    DESCRIPTION = ("This program take an sequence input to output a trajectory"
                   " a 2D or 3D optimized conformation using a Monte Carlo"
                   "algorithm, with Dill's H/P model.")

    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument(
        "-i, -input",
        required=True,
        dest="input",
        type=str,
        help="An input sequence. Could be a literal STRING or a FASTA file."
    )

    # action='store_true' enregistre TRUE, soit bool.

    return vars(parser.parse_args())
