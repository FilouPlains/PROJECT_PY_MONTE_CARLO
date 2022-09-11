# Importation of other python module.
import os
import sys

# Importation of "homemade" python module.
import general_function.parsing as pars
import general_function.translation as trlt
import amino_acid_class.sequence_manipulator as clattrib
import amino_acid_class.coord_manip as cm
import graphic.visual_graphic as visual

if __name__ == "__main__":
    argument = pars.parsing()

    input = argument["input"].lower()

    if input[-3:] == ".fa" or input[-6:] == ".fasta":
        seq_list = pars.fasta_parser(file=argument["input"])
    else:
        if len(argument["input"]) < 2:
                        sys.exit("[Err## 2] Sequence too short.")
        seq_list = [argument["input"].upper()]

    seq_list = trlt.translation(seq_list)

    list_seq_link = []

    for sequence in seq_list:
        list_seq_link += [clattrib.AminoAcidManip(sequence)]

    link_sequence = list_seq_link[0]
    link_sequence.set_path(False)

    patate = link_sequence.get_coord_manip()
    carotte = visual.GraphicalRepresentation(patate.get_coord_list(),
                                             link_sequence.get_sequence_model())
    carotte.draw()
    carotte.display_window()
    
    print("energie =", patate.calc_energy(link_sequence.get_sequence_model()))
    
    link_sequence.end_move(link_sequence.get_link_sequence()[0])
    link_sequence.corner_move(link_sequence.get_link_sequence()[1])
    link_sequence.crankshaft_move(link_sequence.get_link_sequence()[1])
    link_sequence.pull_moves(link_sequence.get_link_sequence()[0])
    
    carotte = visual.GraphicalRepresentation(patate.get_coord_list(),
                                             link_sequence.get_sequence_model())
    carotte.draw()
    carotte.display_window()

# NUMBA = https://numba.pydata.org/ ; DASK = https://www.dask.org/