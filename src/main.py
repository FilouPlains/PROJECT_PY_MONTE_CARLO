# Importation of other python module.
import os
import sys

# Importation of "homemade" python module.
import function.parsing as pars
import function.parsing as pars

if __name__ == "__main__":
    argument = pars.parsing()

    input = argument["input"].lower()

    if input[-3:] == ".fa" or input[-6:] == ".fasta":
        sequence = pars.fasta_parser(file=argument["input"])
    else:
        sequence = argument["input"].upper()

    print(argument["input"])
    print(sequence)


