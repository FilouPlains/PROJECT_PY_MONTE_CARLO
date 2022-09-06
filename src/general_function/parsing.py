"""Functions necessary for the parsing.
"""

# Importation of other python module.
import argparse
import os
import sys


def parsing():
    """This function call the parser to get all necessary program's arguments.

    Returns
    -------
    argparse.ArgumentParser() object
        Permit the accessibility to access to all given arguments with their
        values.
    """
    # Setup the arguments parser object.
    parser = argparse.ArgumentParser()

    # Description of the program given when the help is cast.
    DESCRIPTION = ("This program take an sequence input to output a trajectory"
                   " a 2D or 3D optimized conformation using a Monte Carlo"
                   "algorithm, with Dill's H/P model.")

    parser = argparse.ArgumentParser(description=DESCRIPTION)

    # =======
    # OPTIONS
    # =======

    # == REQUIRED.
    parser.add_argument(
        "-i, -input",
        required=True,
        dest="input",
        type=str,
        help="An input sequence. Could be a literal STRING or a FASTA file."
    )

    # Transform the input into a dictionary with arguments as key.
    argument = vars(parser.parse_args())

    # action='store_true' enregistre TRUE, soit bool.

    return argument


def fasta_parser(file):
    """Parse through a given `.fasta` file to get the sequence(s).

    Parameters
    ----------
    file : string
        The path to the `.fasta` file.

    Returns
    -------
    list
        List of read sequence(s).
    """
    # Checking if the file exists/the path is good.
    if not(os.path.exists(file)):
        sys.exit(f"ERROR: The file '{file}' does not exist (or wrong path"
                 " given).")

    # Reading the given file.
    with open(file, "r", encoding="utf-8") as file_reader:
        seq_list = []
        sequence = ""
        new_seq_to_read = False

        for line in file_reader:
            # Initiate the reading of a new sequence.
            if line[0] == ">":
                if sequence != "":
                    seq_list += [sequence.upper()]
                new_seq_to_read = True
                sequence = ""
                continue
            # Writing a sequence.
            elif new_seq_to_read:
                sequence += line.strip()
            # The `.fasta` file is wrong, error throw.
            else:
                sys.exit(f"ERROR: It's look like your file '{file}' does not"
                         " respect the classical format. Please check it.")

    # Adding the last sequence.
    seq_list += [sequence.upper()]

    return seq_list
