# Importation of other python module.
import os
import sys

# Importation of "homemade" python module.
import general_function.parsing as pars
import general_function.translation as trlt
import amino_acid_class.class_attribution as clattrib

if __name__ == "__main__":
    argument = pars.parsing()

    input = argument["input"].lower()

    if input[-3:] == ".fa" or input[-6:] == ".fasta":
        seq_list = pars.fasta_parser(file=argument["input"])
    else:
        seq_list = [argument["input"].upper()]

    print(argument["input"])
    print(seq_list)

    seq_list = trlt.translation(seq_list)

    print(seq_list)
    
    for sequence in seq_list:
        clattrib.amino_acid_manip(sequence)
        
        for amino_acid in link_sequence:
            print(amino_acid)
