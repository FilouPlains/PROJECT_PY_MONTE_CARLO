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
        seq_list = [argument["input"].upper()]

    seq_list = trlt.translation(seq_list)

    list_seq_link = []

    for sequence in seq_list:
        list_seq_link += [clattrib.AminoAcidManip(sequence)]

    link_sequence = list_seq_link[0]
    link_sequence.set_path(False)

    patate = link_sequence.get_coord_manip()
    carotte = visual.GraphicalRepresentation(patate.get_coord_list())

    carotte.draw_amino_acid(50, 50, "H")
    carotte.draw_amino_acid(50, 90, "P")
    carotte.display_window()
