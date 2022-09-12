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
                   " a 2D optimized\nconformation using a Monte Carlo"
                   " algorithm, with Dill's H/P model.")

    parser = argparse.ArgumentParser(description=DESCRIPTION)

    # =======
    # OPTIONS
    # =======

    # == REQUIRED.
    parser.add_argument(
        "-i, --input",
        required=True,
        dest="input",
        type=str,
        help="An input sequence. Could be a literal STRING or a FASTA file."
    )
    parser.add_argument(
        "-s, --step",
        required=True,
        dest="step",
        type=int,
        help="The number of Monte Carlo step to do."
    )

    # == OPTIONAL.
    parser.add_argument(
        "-tmin, --minimal_temperature",
        required=False,
        dest="tmin",
        type=int,
        help=("An optional integer argument. By default set at 35(°C). The"
              " program will go from\n'tmin' to 'tmax' with a step = 1.")
    )
    parser.add_argument(
        "-tmax, --maximal_temperature",
        required=False,
        dest="tmax",
        type=int,
        help=("An optional integer argument. By default set at 40(°C). The"
              " program will go from\n'tmin' to 'tmax' with a step = 1.")
    )
    parser.add_argument(
        "-pm, --probability_pull_move",
        required=False,
        dest="pm",
        type=float,
        help=("An optional argument. Probability of doing a pull move. By"
              " default set at 0.")
    )
    parser.add_argument(
        "-rp, --random_placement",
        required=False,
        dest="rp",
        action="store_true",
        help=("An optional argument. If `True`, placement the sequence"
              " randomly. Else, if\n`False`, linearly. By default set on"
              " `False`.")
    )

    # Transform the input into a dictionary with arguments as key.
    argument = vars(parser.parse_args())
    argument_list = argument.keys()

    # Default values
    if argument["tmin"] is None:
        argument["tmin"] = 35
    if argument["tmax"] is None:
        argument["tmax"] = 40
    if argument["pm"] is None:
        argument["pm"] = 0

    # Checking if given input are correct.
    if argument["tmax"] < argument["tmin"]:
        sys.exit("[Err## 5] The maximal temperature is inferior to the minimal"
                 " one. Please, invert\nvalue.")
    elif argument["tmax"] <= 0 or argument["tmin"] <= 0:
        sys.exit("[Err## 6] The temperature only accept positive integer.")
    elif argument["pm"] < 0 or argument["pm"] > 1:
        sys.exit("[Err## 7] A probability should be include in [0, 1].")
    elif argument["step"] <= 0:
        sys.exit("[Err## 8] Number of step should at least be 1.")

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
        sys.exit(f"[Errno 2] No such file or directory: '{file}'.")

    # Reading the given file.
    with open(file, "r", encoding="utf-8") as file_reader:
        seq_list = []
        sequence = ""
        new_seq_to_read = False

        for line in file_reader:
            # Initiate the reading of a new sequence.
            if line[0] == ">":
                if sequence != "":
                    if len(sequence) < 2:
                        sys.exit("[Err## 2] Given sequence too short.")

                    seq_list += [sequence.upper()]
                new_seq_to_read = True
                sequence = ""
                continue
            # Writing a sequence.
            elif new_seq_to_read:
                sequence += line.strip()
            # The `.fasta` file is wrong, error throw.
            else:
                sys.exit(f"[Err## 3] The '.fasta' file ('{file}') is in the"
                         " wrong format.")

    # Adding the last sequence.
    seq_list += [sequence.upper()]

    return seq_list
