# Importation of other python module.
import os
import sys

# Importation of "homemade" python module.
import general_function.parsing as pars
import general_function.translation as trlt
import amino_acid_class.sequence_manipulator as seq_manip
import graphic.visual_graphic as visual
import monte_carlo.monte_carlo as mc

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
        list_seq_link += [seq_manip.AminoAcidManip(sequence)]
    
    for seq_list in list_seq_link:
        seq_list.set_path(argument["rp"])
        coord_manip = seq_list.get_coord_manip()

        window = visual.GraphicalRepresentation(coord_manip.get_coord_list(),
                                                seq_list.get_sequence_model())
        window.draw()
        window.display_window()

        monte_carlo = mc.MonteCarlo(
            seq_list,
            argument["tmin"],
            argument["tmax"],
            argument["pm"],
            argument["step"]
        )
        
        monte_carlo.monte_carlo()
        
        window = visual.GraphicalRepresentation(coord_manip.get_coord_list(),
                                                seq_list.get_sequence_model())
        window.draw()
        window.display_window()

    # link_sequence = list_seq_link[0]
    # link_sequence.set_path(False)

    # patate = link_sequence.get_coord_manip()
    
    
    # print("energie =", patate.calc_energy(link_sequence.get_sequence_model()))
    
    # link_sequence.end_move(link_sequence.get_link_sequence()[0])
    # link_sequence.corner_move(link_sequence.get_link_sequence()[1])
    # link_sequence.crankshaft_move(link_sequence.get_link_sequence()[1])
    # link_sequence.pull_moves(link_sequence.get_link_sequence()[0])
    
    # carotte = visual.GraphicalRepresentation(patate.get_coord_list(),
    #                                          link_sequence.get_sequence_model())
    # carotte.draw()
    # carotte.display_window()

# NUMBA = https://numba.pydata.org/ ; DASK = https://www.dask.org/
