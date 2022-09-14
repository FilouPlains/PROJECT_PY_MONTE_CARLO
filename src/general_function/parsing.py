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
    parser.add_argument(
        "-o, --output",
        required=True,
        dest="output",
        type=str,
        help="An csv file to output."
    )

    # == OPTIONAL.
    parser.add_argument(
        "-tmin, --minimal_temperature",
        required=False,
        dest="tmin",
        type=int,
        help=("An optional integer argument. By default set at 35(°C). The"
              " program will go from 'tmin' to 'tmax' with a step = 1.")
    )
    parser.add_argument(
        "-tmax, --maximal_temperature",
        required=False,
        dest="tmax",
        type=int,
        help=("An optional integer argument. By default set at 40(°C). The"
              " program will go from 'tmin' to 'tmax' with a step = 1.")
    )
    parser.add_argument(
        "-co, --cut_off",
        required=False,
        dest="co",
        type=int,
        help=("An optional argument *IF -remc NOT GIVEN*. Energy when to stop"
              " the REMC algorithm (cut-off).")
    )
    parser.add_argument(
        "-ts, --total_step",
        required=False,
        dest="ts",
        type=int,
        help=("An optional argument *IF -remc NOT GIVEN*. Number of REMC step"
              " to do.\n`total_steps = step * total_step * temperature_range`")
    )
    parser.add_argument(
        "-mf, --mol_file",
        required=False,
        dest="mf",
        type=str,
        help=("Write a mol2 file.")
    )
    parser.add_argument(
        "-rp, --random_placement",
        required=False,
        dest="rp",
        action="store_false",
        help=("An optional argument. If `True`, place the sequence randomly."
              " Else, if `False`, linearly. By default set on `False`.")
    )
    parser.add_argument(
        "-remc, --replica_exchange_monte_carlo",
        required=False,
        dest="remc",
        action="store_true",
        help=("An optional argument. If `True`, use the replica exchange Monte"
              " Carlo algoritme (REMC). If `False`, use the Monte Carlo"
              " algoritm.")
    )

    # Transform the input into a dictionary with arguments as key.
    argument = vars(parser.parse_args())

    # Default values
    if argument["tmin"] is None:
        argument["tmin"] = 35
    if argument["tmax"] is None:
        argument["tmax"] = 40

    # Checking if given input are correct.
    if argument["tmax"] < argument["tmin"]:
        parser.print_help()
        sys.exit("\n[Err## 5] The maximal temperature is inferior to the"
                 " minimal one. Please, invert\nvalue.")
    elif argument["tmax"] <= 0 or argument["tmin"] <= 0:
        parser.print_help()
        sys.exit("\n[Err## 6] The temperature only accept positive integer.")
    elif argument["step"] <= 0:
        parser.print_help()
        sys.exit("\n[Err## 8] Number of step should at least be 1.")
    elif argument["remc"]:
        if argument["co"] is None:
            parser.print_help()
            sys.exit("\n[Err## 4] When '-remc' given, you have to give a"
                     " cut-off.")
        elif argument["co"] >= 0:
            parser.print_help()
            sys.exit("\n[Err## 9] The cut-off have to be inferior strictly to"
                     " 0.")
        elif argument["ts"] is None:
            parser.print_help()
            sys.exit("\n[Err## 10] When '-remc' given, you have to give a"
                     " total step.")
    elif os.path.exists(argument["output"]):
        parser.print_help()
        sys.exit(f"\n[Err## 11] The file '{argument['output']}' already exist,"
                 " please change the name.")

    # Checking that the output file is correct
    if argument["output"][-4:] != ".csv":
        parser.print_help()
        sys.exit(f"\n[Err## 12] The file '{argument['output']}' have to be in"
                 " '.csv' format.")
    elif argument["mf"] is not None:
        if argument["mf"][-5:] != ".mol2":
            parser.print_help()
            sys.exit(f"\n[Err## 13] The file '{argument['mf']}' have to be in"
                    " '.mol2' format.")

    # Treating the user input file/sequence.
    input = argument["input"].lower()

    if input[-3:] == ".fa" or input[-6:] == ".fasta":
        seq_list = fasta_parser(file=argument["input"])
    else:
        if len(argument["input"]) < 2:
            sys.exit("\n[Err## 2] Sequence too short.")
        seq_list = [argument["input"].upper()]

    argument["seq_list"] = seq_list

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
                        sys.exit("\n[Err## 2] Given sequence too short.")

                    seq_list += [sequence.upper()]
                new_seq_to_read = True
                sequence = ""
                continue
            # Writing a sequence.
            elif new_seq_to_read:
                sequence += line.strip()
            # The `.fasta` file is wrong, error throw.
            else:
                sys.exit(f"\n[Err## 3] The '.fasta' file ('{file}') is in the"
                         " wrong format.")

    # Adding the last sequence.
    seq_list += [sequence.upper()]

    return seq_list
